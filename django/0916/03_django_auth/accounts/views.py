from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
# 유저 데이터 
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request): # id create
    '''
    1. 회원가입 작성 페이지
    2. 회원가입 로직 (POST) 
    '''
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request): # session create
    '''
    1. 로그인 페이지 (GET)
    2. 로그인 로직 (POST)
    '''
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 인증을 위한 form
        if form.is_valid(): 
            #로그인 함수는 여기서 호출 
            # login(request, user) 이대로만 하면 에러..
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or'articles:index')
    else: # 받을 준비 form -> 
        form = AuthenticationForm()
    context= {
        'form' : form,
    }
    return render(request, 'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@login_required 
def update(request):
    # UserChangeForm
    if request.method =='POST':
        CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_vaild():
            forms.save()
            return redirect('articles:index')
    else:
        form = UserChangeForm(instance = request.user)
        # request.user은 어노이머스 유저를 커버를 못함 -> @login_required 
    context ={
        'form' : form,
    }
    return render(request, 'accounts/update.html')


def users(request):
    # 모든 객체 받아오기
    user_list = get_user_model().objects.all()
    # context에 저장하고 html파일에서 for문으로 출력
    context = {
        'user_list': user_list,
    }
    print(context)
    return render(request, 'accounts/users.html', context)
