import json

def filter(data):
    # 처음은 일단 출력을 해본다.
    even_num = [numbers for numbers in data if numbers %2 ==0]
    odd_num = [numbers for numbers in data if numbers %2]
    #print(odd_num, even_num)
    dic_oddeven = dict(= even_num,=odd_num)
    return dic_oddeven

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    data = open('00_problem_ex.json', encoding='utf8')
    data = json.load(data)
    print(filter(data))
