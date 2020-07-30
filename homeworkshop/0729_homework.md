# 0729_homework

### 1. Type Class

list / set/ str/ dict/ int



### 2. Magic Method

```python
__init__ : 초기화 메서드  어떤 클래스의 객체가 만들어질 때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해준다.

   
__del__ : 객체가 없어질 때 호출되는 메서드
    
__repr__ : 호출하면 출력한다
ex)  
def __repr__(self):
        return self.title
    
__str__ : 특정 객체를 출력(print()) 할 때 보여줄 내용을 정의할 수 있음
```



### 3. Instance Method

- .append(x) : 리스트 뒤에 데이터를 추가
- ' seperate'.join() : 리스트를 seperate를 기준으로 합쳐서 문자열로 배출   

- .remove(x) : 리스트에서 x를 제거한다. x가 없으면 오류 반환

### 4.  Module Import

```python

(a) = fibo

(b) = fibo_recursion

(c) = recursion
```

