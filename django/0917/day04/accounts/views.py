from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserChangeForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm
# import 순서(django에서 권장하는 방식)
# django Coding Style(googling) 참고

'''
future
standard library
third-party
django
local django
try/except
'''

User = get_user_model()
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # request 객체에 메세지 추가하기 
            messages.add_message(request, messages.SUCCESS, 'Congratuation~!')
            return redirect('accounts:user_list')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 세션을 생성해서 데이터베이스에 저장한다 == 로그인.
            user = form.get_user()
            auth_login(request, user)
            return redirect('accounts:user_list')
    
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def user_list(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    print(context)
    return render(request, 'accounts/user_list.html', context)

@require_POST
def delete(request):
    request.user.delete()
    return redirect('accounts:user_list')


def search(request):
    # 1. 사용자가 입력한 검색어를 뽑아낸다.
    # 2. 데이터베이스에서 검색어에 해당하는 데이터를 가져온다.
    # 3. 보여준다.
    query = request.GET.get('query')
    users = User.objects.filter(username__contains=query)  # LIKE(sqld) # QuerySet 반환(0개 이상)
    context = {
        'users': users,
    }
    return render(request, 'accounts/search_result.html', context)


@login_required
def password_update(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save() # 새로운 password 저장
            update_session_auth_hash(request, user) # 암호 변경 시 세션 무효화 방지
            messages.add_message(request, messages.SUCCESS, 'success~!')
            return redirect('accounts:user_list')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password_update.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:user_list')


@login_required 
def update(request):
    # UserChangeForm
    if request.method =='POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_vaild():
            forms.save()
            return redirect('account:user_list')
    else:
        form = CustomUserChangeForm(instance = request.user)
        # request.user은 어노이머스 유저를 커버를 못함 -> @login_required 
    context ={
        'form' : form,
    }
    return render(request, 'accounts/update.html',context)