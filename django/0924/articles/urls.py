from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('votecreate/', views.votecreate, name='votecreate'),
    path('randompage/', views.randompage, name = 'randompage'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]