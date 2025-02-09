from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class UserProfile(AbstractUser):
    username = models.CharField(max_length=15, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=10, blank=False, null=False)
    last_name = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    email_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name="userprofile_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="userprofile_permissions", blank=True)

    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    

