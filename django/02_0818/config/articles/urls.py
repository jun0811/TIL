from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dtl-example/', views.dtl_example),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name ='catch'),
]