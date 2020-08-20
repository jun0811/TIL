from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path("", views.index , name="index") ,
    path("new/", views.new , name="new"), # 추가
    path("create/", views.create, name="create"), # 추가
    path('<int:article_pk>', views.detail,name="detail"), 
    path('<int:article_pk>/delete/>', views.delete, name="delete"), #삭제
    path("<int:article_pk>/edit/", views.edit, name="edit"), # 업데이트
    path("<int:article_pk>/update/", views.update, name="update"), #업데이트
    
]