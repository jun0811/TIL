# 0727_Homework

### 1. 모음은 몇개나 있을까?

```python
def count_vowels(word):
    vowel = 0
    vowel += word.count('a')
    vowel += word.count('e')
    vowel += word.count('i')
    vowel += word.count('u')
    vowel += word.count('o')
    return vowel

print(count_vowels('apple'))
print(count_vowels('banana'))

#####################################
def count_vowels(word):
    vowel = 'AaEeIiOoUu'
    count = 0
    for w in word:
        if w in vowel:
            count +=1
    return count

print(count_vowels('apple'))
print(count_vowels('banana'))
```



### 2.

(4) : 디폴트로 공백이 정해져있다



### 3. 정사각형만 만들기

```python
def only_square_area(width, height):
    area =[]
    for w in width:
        if w in height:
           area += [w*w]
    return area

print(only_square_area([32,55,64],[13,32,40,55])) 
```

