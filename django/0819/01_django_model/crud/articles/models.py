from django.db import models

# Create your models here.
class Article(models.Model):
    # 상속을 받은거 
    title = models.CharField(max_length= 10) #게시글의 제목
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

