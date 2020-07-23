import json

def filter(data):
    # 처음은 일단 출력을 해본다.
    even_num = [numbers for numbers in data if numbers %2 ==0]
    return even_num

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    data = open('00_problem_ex.json', encoding='utf8')
    data = json.load(data)
    print(filter(data))
