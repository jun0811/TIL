# 0722_workshop



### 1. List의 합 구하기

```python
def list_sum(args):
    total = 0
    for i in args:
        total += i
    return total
```





### 2. Dictionar로 이루어진 List의 합 구하기

```python
def dict_list_sum(args):
    total = 0 
    for i in args: 
        a = i['age']
        total += a
    return total
```



### 3. 2차원 Lis의 전체 합 구하기

```python
def all_list_sum(args):
    total = 0
    for i in args:
        for j in i:
            total += j
    return total
```

