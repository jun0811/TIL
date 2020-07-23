# 0723_workshop

### 1.  숫자의 의미

```python
def get_secret_word(asci):
    result=""
    for i in asci:
        result = result+chr(i)
    return result

print(get_secret_word([83,115,65,102,89]))

```



### 2. 내 이름은 몇일까?

```python
def get_secret_number(word):
    num = 0
    for c in word:
        num += ord(c)
    return num

print(get_secret_number('tom'))
```



### 3. 강한이름

```python
def get_strong_word(word_A,word_B):
    A_num=0
    B_num=0
    for i in word_A:
        A_num += ord(i)
    for j in word_B:
        B_num += ord(j)    

    if A_num > B_num:
        return word_A
    else:
        return word_B

print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))
```

