from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model() # 반드시 함수 호출 형태로 작성
        fields = UserCreationForm.Meta.fields + ('email',)
                # ('username', 'password', 'password_confirmation',) + ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)