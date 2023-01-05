from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form for user creation."""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "name",
            "email",
        )


class CustomUserChangeForm(UserChangeForm):
    """Form for update/modify user."""

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "name",
            "email",
        )
