# import sys
# sys.stdin = open('sample_input.txt')
T = int(input())

for tc in range(1,T+1):
    stack = list(input().split()) # 입력
    result = [] # 결과를 위한 스택
    # print(stack)
    error = False
    L = len(stack)
    for i in range(L-1):
        if stack[i].isdigit():
            result.append(int(stack[i]))
        else:
            try:
                if stack[i] =='.':
                    break
                a = result.pop()
                b = result.pop()
                if stack[i] =='+': c = b+a
                elif stack[i] == '*': c = b *a
                elif stack[i] == '/': c = b //a
                elif stack[i] == '-': c = b-a
                result.append(c)
            except:
                error = True
    if error or len(result)>1:
        print('#{} error'.format(tc))
    else:
        print('#{} {}'.format(tc, *result))
