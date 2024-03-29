# 0922Practice

### * 환경설정

- 가상환경
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py loaddata users/users.json
  - fixtures는 생략된것
- python manage.py shell_plus



### 1. user 테이블 전체 데이터 조회

```python
User.objects.all()

# queryset 출력
query = User.objects.all().query 
>>> print(query)
```



### 2. id가 19인 사람의 age를 조회 

```python
User.objects.filter(id=19).values('age')
```



### 3.  모든 사람의 age를 조회

```python
User.objects.all().values('age')
```



### 4. age가 40이하인 사람들의 id와 balance를 조회

```python
User.objects.filter(age__lte=40).values('id', 'balance')
```



###  5. last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회

```python
User.objects.filter(last_name='김', balance__gte=500).values('first_name')
```



### 6.  first_name이 '수'로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회

```python
User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
```



###  7.  balance가 2000 이상이거나 age가 40이하인 사람의 총 인원수를 구하시오. 

```python
from django.db.models import Q
User.objects.filter(
  Q(age__lte=40) | Q(balance__gte=2000)
).count()
```



### 8.  phone 앞자리가 ‘010’으로 시작하는 사람의 총원구하기 

```python
 User.objects.filter(phone__startswith='010').count()
```



### 9.  이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오.

```python
>>> user = User.objects.get(first_name='옥자', last_name='김')
>>> user.country = '경기도'
>>> user.save()
>>> user.country
'경기도'
```



###  10.  이름이 ‘백진호’인 사람을 삭제하시오.  

```python
>>> user = User.objects.get(first_name='진호', last_name='백').delete()
>>> User.objects.all().count()
99
```



### 11.  balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오. 

```python
User.objects.order_by('-balance')[:4].values('first_name', 'last_name', 'balance')
```



### 12.  phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오.

```python
User.objects.filter(phone__contains='123', age__lt=30)
```



### 13.  phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오. 

```python
User.objects.filter(phone__startswith='010').values('country').distinct()
```



### 14.  모든 인원의 평균 age를 구하시오. 

```python
User.objects.aggregate(Avg('age'))
```



### 15.  박씨의 평균 balance를 구하시오. 

```python
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```



### 16.  경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오. 

```python
User.objects.filter(country='경상북도').aggregate(Max('balance'))
```



### 17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오. 

```python
User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[0]
```



