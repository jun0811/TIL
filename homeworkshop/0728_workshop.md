# 0728_workshop

### 1. 무엇이 중복일까

```python 
#문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters
def duplicated_letters(word):
    result = { }
    duplic = []
    for w in word:
        if not w in result:
            result[w] = 1
        else:
            result[w] +=1
    for key, val in result.items():
        if result[key] > 1:
            duplic.append(key)
    return duplic

##############################################
def duplicated_letters(word):
    duplicates = []
    for word in words:
        if words.count(word) > 1 and word not in duplicates:
            duplicates.append(word)
    return duplicates
```



### 2. 소대소대

```python
def low_and_up(word):
    result =[]
    n=1 
    for w in word:
        if n%2:     
            result.append(w.lower())
        else:
            result.append(w.upper())
        n += 1 
    return ''.join(result)

print(low_and_up('apple'))
```



### 3. 

```python
def lonely(numbers):
    # 연속 숫자이면 하나만 반환
    n = 0
    result = []
    for num in numbers:
        if not num in result:
            result.append(num)
        else:
            #있으면 둘의 인덱스를 체크 ?
            if numbers[n] != numbers[n-1]:
                result.append(num)
        n += 1
    return result
#########
def lonely(numbers):
    result =[]
    for idx,num in enumerate(numbers):
        if idx == 0:
			result.append(num)
        if result[-1] != num:
            result.append(num)
    return result
```

