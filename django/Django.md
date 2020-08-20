# Django

### 1. url 분리

1) 프로젝트의 urls.py에서 app 마다 경로를 분리한다

```python
from django.contrib import admin
from django.urls import path, include
 
# 앱별로 url 분리 -> include

urlpatterns = [
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]

```



2) app -> urls.py 만들고 밑에 처럼 작성

```python
from django.urls import path
from . import views

app_name = 'articles' # -> 경로설정을 편하게 하기 위해서 한것

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dtl-example/', views.dtl_example),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name ='catch'),
]
```



3) views.py

```python
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def dtl_example(request):
    meuns = ["짜장면", "탕수육", "양장피"]
    my_sentence = "life is short, you need python"
    message = ["apple", "banana, mango", "watermelon"]
    datetime_now = datetime.now()
    empty_list = []
    context = {
        "menus" : meuns,
        "my_sentence": my_sentence,
        "message" : message,
        "datetime_now" : datetime_now,

    }
    return render(request, 'articles/dtl_example.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    username = request.GET.get("username")
    print(username)
    context = {
        "username" : username
    }
    return render(request,'articles/catch.html',context)


# app -> templates 생성후 -> articles -> 'xx.html'
# 이것을 해주는 이유는 
```





##### (1) 같은 이름 다른 app의 구분 방법





### 2. templates 상속

1. project 안에 templates 폴더를 만든다

2. 상속할 html 파일을 만든다

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=
     , initial-scale=1.0">
     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
     <title> 
     {% block title%}
         Template Inheritance
     {% endblock %}
     </title>
   </head>
   <body>
     <div class = "container">
       {% block content %}
       <!-- content 이름은 아무거나 .. -->
       {% endblock %}
     </div>
     <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
   <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
   <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

3.  상속받을 파일은 이와 같이 작성

   ```html
   <!-- 최상단에 상속 -->
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>즐거운 Django</h1>
   {% endblock %}
   
   
   {% block title%}
    	NEW TITLE 
     {% endblock%}
   ```

4. settings.py

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR / 'config' / 'templates'],
           # 경로를 나눈다? base_dir이 절대경로를 다본다
           'APP_DIRS': True, # 프로젝트에 만든 템플릿은 app_dirs가 보지 못한다.
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   
   
   
   BASE_DIR = Path(__file__).resolve(strict=True).parent.parent 
   # 경로 설정해주는 문구
   ```

   



