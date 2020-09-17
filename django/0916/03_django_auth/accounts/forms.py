# UserChangeForm 커스터마이징
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    # 필드가 다보여서 부분적으로  
    class Meta:
        model = User
        fields = ('first_name' , 'last_name', 'email',)