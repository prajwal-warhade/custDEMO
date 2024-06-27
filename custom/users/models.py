from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    unique_identity_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username
