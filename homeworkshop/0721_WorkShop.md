## 0721 WorkShop



### 1. 간단한 N의 약수

```python
# N의 약수
while True:
    N = int(input("N은 1이상 1000이하:"))
    if 1<= N <= 1000:
        break
    else:
        continue

for i in range(1, N+1):
    if(N%i==0):
        print(i, end=" ")
    
```

### 2. 중간값 찾기

```python
numbers = [
    85,72,38,80,69,65,68,96,22,49,67,
    51,61,63,87,66,24,80,83,71,60,64,
    52,90,60,49,31,23,99,94,11,25,24
]
len_numbers = len(numbers)

sorted_numbers = sorted(numbers)

print(sorted_numbers[len_numbers//2])

```





### 3. 계단 만들기

```python
#  계단 만들기 
N = int(input("자연수"))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
```

### 4. 구구단

```python
#구구단 
for i in range(2,10):
    print(f'----{i}단----')
    for j in range(1,10):
        print(f'{str(i)} X {str(j)} = {i*j}')
```

