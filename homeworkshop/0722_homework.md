# 0722_homework



### 1.  Built-in 함수

```python
'''
print  sum  type  divmod  max  min  len  sorted enumerate  
'''
```



### 2. 정중앙 문자

```python
def get_middle_char(word):
    if len(word)%2 == 0:
        return word[len(word)//2-1:len(word)//2+1]
    else:
        return word[len(word)//2]
```



### 3. 위치 인자와 키워드 인자

(4)

디폴트가 없는 인자는 앞에 있어야합니다.



### 4. 나의 반환값은

None

함수에 리턴값이 존재하지 않습니다.



### 5. 가변인자 리스트

```python
def my_avg(*args):
    return sum(args)/len(args)

```

