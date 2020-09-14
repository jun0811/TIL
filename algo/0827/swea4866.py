
T = int(input())

for tc in range(1,T+1):
    String = input()
    length = len(String)
    stack = []
    result = 1
    # print(String)
    for i in range(length):
        if String[i] == '{' or String[i] == '(':
            stack.append(String[i])
        elif String[i] == '}' or String[i] ==')':
            if len(stack) == 0: #없는데 호출 당했으면
                stack.append(-1)
                break
            if (stack[-1] != '{' and String[i]== '}') or (stack[-1] != '(' and String[i]== ')') : #마지막 꺼랑 쌍을 이루지 않으면 에러
                stack.append(-1)
                break
            stack.pop()
    if not len(stack):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
