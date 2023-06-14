from django.urls import path

from .views import SignUp, MyTokenObtainPairView
from rest_framework_simplejwt.views import  TokenRefreshView


urlpatterns = [
    path('signUp',SignUp.as_view()),
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]