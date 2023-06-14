from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    profile_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    pic = models.CharField(max_length=100)