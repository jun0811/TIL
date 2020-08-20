# 0819 model

- 스키마
- 테이블
- pk (기본키) : 각행의 고유값 -> primary Key
  - 데이터 베이스 관리 및 관계 설계시 중요
- 행/열/레코드



### model 

> 위를 조작하는것이 model  / 가장 먼저 정의



- app -> models.py

  ```python
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      # 상속을 받은거 
      title = models.CharField(max_length= 10) #게시글의 제목
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add= True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

  





##### ORM

>객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 데이터를 변환하는 프로그래밍 
>
>기술

- 장점 : sql을 몰라도 된다  / 객체 지향적 조작으로 생산성 good!
- 단점 : ORM만으로 완전한 서비스를 구현하기 어려운 경우



현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것. (생산성)이 중요하여 ORM을 사용한다



---



### CharField(max_length = None)

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max_length가 필수 인자 
- 필드의 최대 길이, 데이터베이스와 Django의 유효성검사 



### TextField()

- 글자의 수가 많을 때 사용
- `<textarea>`  을 사용



### DateTimeField()

- 최초 생성일자 : auto_now_add = True
  - ORM이 최초 데이터 입력시에만 갱신
  - 테이블에 어떤 테이터를 최초로 넣을 떄 
- 최종 수정 일자 : `auto_now= True`
  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신 

https://docs.djangoproject.com/en/3.1/ref/models/fields/











## Migrations

- `python manage.py makemigrations`: 으로 만들어주기 (변경사항이 있을 때마다 꼭 해주기!!)

  - 모델을 변경한 것에 기반한 새로운 마이그레이션(설계도) 을 만들 때 사용
  - 모델을 활성화 하기 전에 DB설계도를 작성 
  - 생성된 마이그레이션 파일은 데이터베이스 스키마를 위한 버전관리 시스템이라고 생각

  

- model -> migration 을 통해 파이썬 코드가 sql문을 확인 가능

- `python manage.py sqlmigrate articles 0001`   : 해당 마이그레이션 파일이 sql문으로 어떻게 해석되어 동작할지 미리 확인하기 위한 명령어 

- `python manage.py migrate`   : table 만들기
  - 작성된 마이그레이션 파일들을 기반으로 실제 DB에 반영 
  - db.sqlite3 라는 데이터베이스 파일에 테이블을 생성
  - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

ex) 앱이름_클래스명 테이블 과 그 밑에 있는 스키마들을 확인 가능 



- `showmigrations`명령어 : 내가 진행한 마이그레이션 생성 여부 확인 



##### Model 중요 3단계

1. models.py 변경사항(작성,수정, 삭제) 발생
2. 설계도 만들기 : 설계도 만들기 
3.  migrate : DB에 적용

↪DB가 생성  

database API를 통해 DB를 조작



## DB API

#### Manager

- django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
- 기본적으로 모든 django 모델 클래스에 objects라는 Manager를 추가



#### QuerySet

- 데이터베이스로부터 전달받은 객체 목록
- queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
- 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음

```python
Article.object.all()
# Article과 all부분만 변경
# 순수한 python문법이 아닌 django manager에서 운용되는 문법
```



### orm



pip install ipython django-extensions

python manage.py shell_plus



```shell
# article.save() 이후에 저장 가능(어떤 값을 저장할 때 마다 실행시켜줘야함)
In [10]: article1.save()

In [11]: article1.content = '재밌어용'

In [12]: article2 = Article()

In [13]: article2.save()

In [14]: article2.title = '핸젤과 그레텔'

In [15]: article3 = Article.objects.create(title='clean code', content='masterpiece')

In [17]: Article.objects.all()
Out[17]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]> 
# 쿼리셋은 리스트는 아니지만 리스트에서 사용할 수 있는 것들을 많이 사용 가능 

In [18]: articles = Article.objects.all()

# 인덱싱이 가능
In [19]: articles[0]
Out[19]: <Article: Article object (1)>

# 슬라이싱도 가능하다.
In [21]: articles[1:]
Out[21]: <QuerySet [<Article: Article object (2)>, <Article: Article object (3)>]>

# 음수인덱싱은 지원하지 않는다.
In [22]: articles[-1]
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-22-cbf1974f6304> in <module>
----> 1 articles[-1]

~\AppData\Local\Programs\Python\Python37\lib\site-packages\django\db\models\query.py in __getitem__(self, k)
    302                 (isinstance(k, slice) and (k.start is None or k.start >= 0) and
    303                  (k.stop is None or k.stop >= 0))), \
--> 304             "Negative indexing is not supported."
    305
    306         if self._result_cache is not None:

AssertionError: Negative indexing is not supported.

# 바로 title을 붙이면 list에 붙기때문에 오류
In [24]: articles.title
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-24-acc5ba5ea77e> in <module>
----> 1 articles.title

AttributeError: 'QuerySet' object has no attribute 'title'

# 인덱싱으로 뽑아내서 title을 붙이면 가능함을 알 수 있다.
In [25]: articles[0].title
Out[25]: ''

# get사용하기 (1번 키를 가져오기(pk:primary key))
In [26]: article1 = Article.objects.get(pk=1)

In [27]: article1
Out[27]: <Article: Article object (1)>


# 없는 객체를 가져오려 하니 오류가 난다.
# 필터를 통해 아무것도 반환이 안되면 None이 반환
In [30]: Article.objects.get(pk=10000000)
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-30-3bbe0657b583> in <module>
----> 1 Article.objects.get(pk=10000000)

~\AppData\Local\Programs\Python\Python37\lib\site-packages\django\db\models\manager.py in manager_method(self, *args, **kwargs)
     83         def create_method(name, method):
     84             def manager_method(self, *args, **kwargs):
---> 85                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     86             manager_method.__name__ = method.__name__
     87             manager_method.__doc__ = method.__doc__

~\AppData\Local\Programs\Python\Python37\lib\site-packages\django\db\models\query.py in get(self, *args, **kwargs)
    429             raise self.model.DoesNotExist(
    430                 "%s matching query does not exist." %
--> 431                 self.model._meta.object_name
    432             )
    433         raise self.model.MultipleObjectsReturned(

DoesNotExist: Article matching query does not exist.

# 삭제하기
In [31]: article1 = Article.objects.get(pk=1)

In [32]: article1.delete()
Out[32]: (1, {'articles.Article': 1})

In [33]: article1
Out[33]: <Article: Article object (None)>

# 수정하기
In [34]: article2 = Article.objects.get(pk=2)

In [35]: article2.title = 'Algorithm'

In [36]: article2.save()
```

```python
#Article()클래스 활용 인스턴스(db의 실제 데이터) 생성
#생성 방법 1
article1 = Article()
article.save() # 반드시 save를 해야지 db에 반영
article1.title = 'atomic habit'
article1.content = 'lorem klsdj dslkjl lkjsd'
article.save()
article2 = Article()
article2.title = 'Little princess'
article2.content = 'asdfsd'
article2.save()
#생성 방법 2
article3 = Article.objects.create(title='clean code', content='masterpiece')
# class.manager.querysetAPI
# create querysetAPI 활용
# manager를 활용하면 save를 하지 않아도 된다. 
#=================quertsetAPI 활용================================
#querysetAPI all() ==> queryset 반환
articles = Article.objects.all() #모든 테이블의 객체를 저장
articles #QuerySet, list는 아니지만 비슷하게 활용 가능
#querysetAPI get() ==> 객체(instance) 반환
article1 = Article.objects.get(pk=1) # 객체 반환 
#없는 pk를 요청하면 error
Article.objects.get(pk=1000000)
#querysetAPI filter() ==> queryset 반환
articles = Article.objects.filter(title='Little princess')
#없는 field요청하면 empty queryset 반환
Article.objects.filter(title='존재하지 않는 이름')
#==================delete()=====================
article1 = Article.objects.get(pk=1)
#delete()시 tuple반환, save안해도 db반영
article1.delete()
#===================update==========================
article2 = Article.objects.get(pk=2)
article2.title = 'Algorithm'
article2.save()
```



## READ

`all`

- `QuerySet` return
- 리스트는 아니지만 



`get()`

- 객체가 없으면 `DoesNotExitst`에러가 발생
- 객체가 여러개일 경우는 `MultipleObjectReturned` 에러가 발생
- 위와 같은 특징을 가지고 있기 때문에 unique 혹은 Not Null 특징을 가지고 있으면 사용할 수 있다.  (pk값을 통해 조회)







DB구축하고 -> 슈퍼 유저 만들기

- 슈퍼 유저 만들기

  `python manage.py createsuperuser` 

##### admin.py

```python
from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)
```

