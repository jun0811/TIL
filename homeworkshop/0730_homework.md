# 0730_homework

###  1. Circle 인스턴스 만들기

```python


class Circle:

  pi = 3.14

  

  def __init__(self,r,x,y):

        self.r = r
        self.x = x
        self.y = y



  def area(self):

	return self.pi*self.r*self.r





  def circumference(self):
	return 2 * self.pi * self.r



  def center(self):
        return (self.x, self.y)





C1 = Circle(3,2,4)

print(f'둘레 {C1.circumference()} 넓이 {C1.area()}')
```



### 2. dog과 bird는 animal이다

```python
class Animal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    
    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.walk()
```



### 3. 오류의 종류

```python
ZeroDivisionError : 0으로 나누는 경우
NameError : 이름이 없는 경우
TypeError : 타입이 맞지 않는 경우
IndexError : 인덱스에 벗어난 경우
KeyError :  파이썬 사전(Dictionary)에서 발생하는 오류
ModuleNotFoundError ; import하면서 경로나 현재 디렉토리에 import 할 대상을 찾게 못할 때.
ImportError : 임포트가 안된 경우
```

