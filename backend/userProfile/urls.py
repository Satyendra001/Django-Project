from django.urls import path

from .views import NewProfile, UpdateProfile

urlpatterns = [
    path('newProfile', NewProfile.as_view()),
    path('updateProfile', UpdateProfile.as_view()),
]