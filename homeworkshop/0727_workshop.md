# 0727 Workshop

### 1. 평균점수 구하기

```python
def get_dict_avg(score):
    total = 0
    for key in score:
        total += score[key]
    return total/len(score) # 딕셔너리도 len 사용이 가능하다...!!

print(get_dict_avg({'py':90, 'algo':80, 'django': 89, 'web':83}))
```



### 2.  혈액형 분류하기 

```python
def count_blood(blood):
    blood_counter = {'A': 0, 'B':0, 'O':0, 'AB':0, }
    for key in blood_counter:
        if key in blood:
            blood_counter[key] +=1
        
    return blood_counter

print(count_blood(['A','B','A','O','AB']))
```

