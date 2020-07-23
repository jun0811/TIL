# 0720_WorkShop

# 1. 세로로 출력하기

```python
number = int(input())

# 아래에 코드를 작성하시오.
for i in range(1, number+1):
    print(i)
```



# 2. 가로로 출력하기

```python
number = int(input())
# 아래에 코드를 작성하시오.
for i in range(1,number+1):
    print(i, end= ' ')
```





# 3.거꾸로 세로로 출력하기

```python
number = int(input())
while number>=1:
    print(number)
    number -=1
```



# 4. 거꾸로 출력해보아요

```python
number = int(input())

# 아래에 코드를 작성하시오.
while number >=0:
    print(number, end =" ")
    number -=1
```



# 5.  N줄 덧셈 (SWEA #2025)

```python
number = int(input())
sum= 0
# 아래에 코드를 작성하시오.
for i in range(1, number+1):
    sum+=i

print(sum)
```

