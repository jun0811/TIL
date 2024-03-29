from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('',views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/',views.create, name="create"),
    path('<int:article_pk>/detail', views.detail, name = "detail"),
    path('<int:article_pk>/edit', views.edit, name = "edit"),
    path('<int:article_pk>/update', views.update, name = "update"),
    path('<int:article_pk>/delete', views.delete, name = "delete"),
]
