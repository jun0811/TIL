from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser): # 상속 받는것 : abstractUser ,  User를 상속을 받지 않는 이유 : ??? 
    pass # settings.py -> AUTH_USER_MODEL = 'accounts.User' 추가 
    # articles (model.py)으로 이동 