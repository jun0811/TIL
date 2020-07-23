# 0720_HOMEWORK

# 1.Python 예약어

답안

```python
'''True/False/None/and/as/assert
break/def/class/else/from/if/import
except'''

```



# 2. 실수비교

```python
num1 = 0.1 * 3
num2 = 0.3
import math
# 아래에 답안을 작성하시오.
print(math.isclose(num1,num2))

#########################################################
print(round(num1,2) == num2)
```



# 3. 이스케이프 시퀀스

```python
# 아래에 답안을 작성하시오.
print("\n")
print("\t")
print("\b")
```



# 4. String Interpolation

```pyhton
name = '철수'

# 아래에 답안을 작성하시오.
print("나의 이름은 %s" %name)
print(f'나의 이름은 {name}')
print("나의 이름은 {0}".format(name))

```



# 5. 형 변환

```python
str(1) # (1)  O
int('30') # (2) O
int(5) # (3) O
bool('50') # (4) O
int('3.5') # (5) X
```



# 6. 네모 출력

```python
n = 5
m = 9
a = "*"*n+"\n"
print(a*m)
# 아래에 답안을 작성하시오.
### or ###
n = '*'*n
print((f'{n}\n')*m)
```



# 7. 이스케이프 시퀀스 응용

```python
# 아래에 답안을 작성하시오.
print('''
"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."
나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.
'''
)

```



# 8. 근의 공식

```python
# 아래에 답안을 작성하시오.
a = float(input(''))
b = float(input(''))
c = float(input(''))
root1 = ((-b) + ((b**2)-(4*a*c))**(0.5)) /2/a
root2 = ((-b) - ((b**2)-(4*a*c))**(0.5)) /2/a

print(f'x1 = {root1:.2f}, x2 = {root2:.2f})

#### or ###
# 아래에 답안을 작성하시오.
a = float(input(''))
b = float(input(''))
c = float(input(''))
D = (b*b - 4*a*c)**(0.5)
x1 = ((-b) + D) / (2*a)

x2 = ((-b) - D) / (2*a)

print('x1 : {0}'.format(x1))
print('x2 : {0}'.format(x2))

```

