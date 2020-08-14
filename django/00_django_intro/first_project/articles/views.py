# django imports style guide
# 1. standard library
# 2. 3rd party
# 3. Django
# 4. local django
import random
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = { 
        'pick' : pick
    }
    return render(request, 'dinner.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)

def dtl_practice(request):
    menus = ['a' , 'b', 'c']
    empty = []
    context = {
        "menus" : menus,
        "empty" : empty,
    }
    return render(request,'dtl_practice.html',context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # 받은 폼데이터를 어떻게 가져오지??
   
    message = request.GET.get('name') # 에러가 나지 않게 .. get을 쓰자
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)