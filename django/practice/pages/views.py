from django.shortcuts import render
import requests
import random
# Create your views here.
def random_num(number):
    set1 = set(number[:6])
    # print(set1)
    lotto = range(1,46)
    grade = {'1등': 0 ,'2등':0 ,'3등':0, '4등':0 ,'5등': 0, '꽝': 0}
    for _ in range(1000):    
        my_number = random.sample(lotto, 6)
        my_number.sort()
        set2 = set(my_number)
        inter = set1 & set2
        if len(inter) == 6:
            grade['1등'] +=1
        elif len(inter) == 5:
            if number[6] in my_number:
                grade['2등'] +=1
            else:
                grede['3등'] +=1
        elif len(inter) == 4:
            grade['4등'] +=1
        elif len(inter) == 3:
            grade['5등'] +=1
        else:
            grade['꽝'] +=1    
    return grade
def lotto(request):
    #이번 회차 924
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=924' 
    response = requests.get(url).json()
    number= []
   
    
    for i in range(1,7):
        text= 'drwtNo' + str(i)
        number.append(response.get(text))
    number.sort()
    number.append(response.get('bnusNo'))
    context = random_num(number)
    context['this'] = number[:6]
    context['bns'] = number[6]


    return render(request, 'lotto.html', context)