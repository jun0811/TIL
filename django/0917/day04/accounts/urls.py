from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.user_list, name='user_list'),
    path('delete/', views.delete, name='delete'),   # 회원탈퇴
    path('search/', views.search, name='search'),
    path('password_update/', views.password_update, name = 'password_update'),
    path('logout/', views.logout, name = 'logout'),
    path('update/', views.update, name = 'update'),
]