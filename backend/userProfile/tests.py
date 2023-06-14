from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

from .models import Profile
from .views import NewProfile, UpdateProfile


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        self.profile_data = {
            "profile_id": 1,
            "name": "Test user",
            "email": "testuser@example.com",
            "bio": "My test Bio",
            "pic": "profile.jpg",
        }

        self.new_profile_url = "/profile/newProfile"
        self.update_profile_url = "/profile/updateProfile"

    def test_create_new_profile(self):
        url = self.new_profile_url

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data=self.profile_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {"response": {"success": "New profile created successfully"}}
        )

    def test_update_profile(self):
        # Create a profile to update
        profile = Profile.objects.create(
            user=self.user,
            profile_id=2,
            name="John Doe",
            email="johndoe@example.com",
            bio="Test Bio",
            pic="profile.jpg",
        )

        url = self.update_profile_url

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            url + "?profile_id=2", data={"email": "newemail@example.com"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"response": {"success": "Profile Patched"}})

        # Refresh the profile from the database to check if it was updated
        profile.refresh_from_db()
        self.assertEqual(profile.email, "newemail@example.com")
