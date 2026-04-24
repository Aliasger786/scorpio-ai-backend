"""
User models for Aura AI authentication."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid
import bcrypt


class User(AbstractUser):
    """Custom user model extending Django's AbstractUser."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    class Meta:
        app_label = 'users'
        db_table = 'users'
