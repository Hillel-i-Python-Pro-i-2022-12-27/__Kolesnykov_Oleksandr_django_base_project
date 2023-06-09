from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "photo",
        )


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
