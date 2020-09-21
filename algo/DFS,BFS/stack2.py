T = int(input())

for tc in range(1,T+1):
    N = input()
    stack = []
    for word in N:
        if word == '{' or word == '(':
            stack.append(word)
        elif word =='}' or word == ')':
            if len(stack) == 0:
                stack.append(-1)
                break
            if (stack[-1]!= '{' and word == '}' or (stack[-1]!='(' and word ==')')):
                stack.append(-1)
                break
            stack.pop()

    if not len(stack): 
        print(1)
    else:
        print(0)
    