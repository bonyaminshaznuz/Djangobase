from django.db import models
from django.contrib.auth.models import AbstractUser


class Custom_User(AbstractUser):
    user_type = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]   
    user_type = models.CharField(choices=user_type, max_length=20)
    profile_image = models.ImageField(upload_to="Media/Profile_pic", blank=True, null=True)

class profile(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)