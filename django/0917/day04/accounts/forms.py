from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Mate:
        model = User
        fields = ('first_name', 'last_name', 'email', )