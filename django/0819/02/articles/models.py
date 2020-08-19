from django.db import models

# Create your models here.
class Article(models.Model):
    # 타입을 결정
    title =  models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True) # 레코드가 데이터베이스 들어가는 첫 순간
    updated_at = models.DateTimeField(auto_now= True) # 이후에 계속 수정 가능 