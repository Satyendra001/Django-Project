from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Profile
from .serializers import ProfileSerializer


def is_valid_email(email):
        email_validator = EmailValidator()
        try:
            email_validator(email)
            return True
        except ValidationError:
            return False


class NewProfile(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        logged_user = request.user.username

        profile_id = request.data.get("profile_id")
        name = request.data.get("name")
        email = request.data.get("email")
        bio = request.data.get("bio")
        pic = request.data.get("pic")
        

        # Validate field values
        if not (profile_id and name and email and bio and pic):
            return Response({"response": {"error": "Empty fields"}}, 400)
        
        # Validate the email
        if not is_valid_email(email):
            return Response({"response": {"error": "E-mail address is invalid"}}, 400)

        # Get the user object for the logged in user
        user_obj = User.objects.get(username=logged_user)

        # validate if profile_id already exists for the logged in user
        try:
            profile = Profile.objects.get(user=user_obj,profile_id=profile_id)
            if profile:
                return Response({"response":{"error": "Profile id already exists"}}, 400)
        except Profile.DoesNotExist:
            print("Profile does not exists, creating a new profile")

        # create the profile and save it
        Profile.objects.create(
            user= user_obj,
            profile_id= profile_id,
            name= name,
            email= email,
            bio= bio,
            pic= pic
        )

        return Response({"response":{"success":"New profile created successfully"}})

class UpdateProfile(UpdateAPIView):
    permission_classes=[IsAuthenticated, ]

    # Define the serializer for the Profile Model
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def patch(self, request):
        logged_user = request.user.username
        data = request.data 

        # Retrieve id of the Profile which the current logged_in user wants to Patch
        id = request.query_params.get("profile_id")

        # Validate the Email if provided
        email = request.data.get("email")
        if email and not is_valid_email(email):
            return Response({"response": {"error": "E-mail address is invalid"}}, 400)

        # Get the user object for the logged in user
        user_obj = User.objects.get(username=logged_user)
        
        if id:
            try: 
                profile = self.queryset.get(profile_id=id, user=user_obj)

                serializer = self.get_serializer(profile, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response({"response": {"success": "Profile Patched"}})
            except Exception as e:
                return Response({"response":{"error": str(e)[:-1] + " as Profile Id not found for the user"}}, 400)
        
        else:
            return Response({"response": {"error": "Id not found!"}}, 400)
        



