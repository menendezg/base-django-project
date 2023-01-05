from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user class representation for puppy-net."""
    name = models.CharField(max_length=200)

