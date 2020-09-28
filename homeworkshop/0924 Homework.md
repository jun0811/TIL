# 0924 Homework



### 1. 

1. T
2. T
3. F 



### 2.

a : user (or request.user)

b : article.like_users.all

```html
{% if user in article.like_users.all %}
```



### 3.

- a) user_pk

- b) follwers

- c) filter

- d) remove

- e) add

  

### 4. 

auth.User에러가 발생하는 이유

-> UserCreationForm 은 auth.User모델을 사용한다.

그러나 현재 User Model을 커스텀 하였으므로 UserCreationForm 또한 커스텀 해야한다.

```python
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
```



### 5. 

M:N 관계 설정 시에 `related_name`이 없다면 자동으로 `article_set`매니저를 사용하게끔 되어있다. 그러나 이 매니저는 이미 `user`필드 에서 사용중이므로 충돌이 발생하게 된다.



### 6. 

a) person.follwings.all

b) person.follwers.all

c) user

d) person

e) person.username







