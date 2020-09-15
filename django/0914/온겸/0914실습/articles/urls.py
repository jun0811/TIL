from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # READ - 전체 게시글 목록
    # http://localhost:8000/articles/
    path('', views.index, name='index'),

    # CREATE
    # path('new/', views.new, name='new'), # 게시글 작성 폼을 보여주는 경로
    path('create/', views.create, name='create'), # 사용자가 보낸 데이터를 처리하는 경로
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
]
