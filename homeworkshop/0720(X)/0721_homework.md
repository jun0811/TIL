## 1. Mutable & Immutable 

mutable : list dict set

immutable : string, integer, float, boolean, tuple, range

---





### 2. 홀수만담기

```python
odd= list(range(1,51,2))
print(odd)
```



### 3. Dictionary 만들기

```python
dic1 = {'이승준': 27, '김지수': 28, '곽온겸': 27}
```



### 4. 반복문으로 네모 출력

```python
n = 5
m = 9

for i in range(0,m):
    print("*"*n)
    
    
### or ###

n =5 
m= 9
for i in range(0,m):
    for j in range(0,n):
        print("*",end="")
    print('')
```



### 5. 조건 표현식

```python
temp = 36.5
print('입실불가') if temp >37.5 else print('입실가능')
```



### 6. 평균 구하기

```python
scores = [80, 90, 99, 83]
sum = 0
for i in scores:
    sum +=i

avg = sum/len(scores)
print(avg)
```

