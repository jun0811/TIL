import sys
def check(arr):
    maxV = 0
    for i in range(0,100):
        for j in range(0,100):
            if arr[i:j+1] == arr[i:j+1][::-1]:
                if maxV < len(arr[i:j+1]):
                    maxV = len(arr[i:j+1])
    return maxV

T = 10
sys.stdin = open('input.txt','r')
for tc in range(1,T+1):
    t = input()
    square = [input() for _ in range(100)]
    max_len = 0
    result = 0
    for s in square: # 가로
        result = check(s) 
        if max_len <= result:
            max_len = result

    Sero_list = []
    sero = ''

    for i in range(len(square)): #세로 
        for s in square:
            sero += s[i]
        Sero_list.append(sero)
        sero = ''

    for s in Sero_list:
        result = check(s) 
        if max_len < result:
            max_len = result
        
    print('#{} {}'.format(t, max_len))