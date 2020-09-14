import sys
sys.stdin = open('input.txt')




for tc in range(1,11):
    N = int(input())
    Data = input()    
    stack = []
    icp = {'(':3 ,'*': 2, '-': 1, '+':1, '*': 2 , '/':2 , } # 넣을 때 
    isp = {'(':0 ,'*': 2, '-': 1, '+':1, '*': 2 , '/':2 , } # 스택 안
    numbers = []
    std = '*/+-('
    # num = '0123456789'
    # 후위 표기법 변경 
    for ch in Data:
        if ch.isdigit():
            numbers.append(ch)
        elif ch in std:
            if len(stack) == 0 or icp[ch] > isp[stack[-1]]: # 새로 집어넣거나 
                stack.append(ch)
            else: 
                while icp[ch] <= isp[stack[-1]]: # 스택 top에 있는 것이 우선순위가 더 높으면 뱉는다. 
                    numbers.append(stack.pop())
                stack.append(ch)
        elif ch == ')': #오른 괄호를 만나면 
            while stack[-1] != '(': # 만날 때까지 돌린다. -> 오른 괄호는 버린다 .
                numbers.append(stack.pop())
            stack.pop() # 짝을 이룬 왼쪽 괄호를 버린다. 
    print(numbers)
    # print(stack)
        # step 2: 
        # 피연산자는 스택에 push -> 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고,
        # 연산결과를 다시 스택에 push
        
    for n in numbers: 
        if n.isdigit():
            stack.append(int(n))
        else:
            a = stack.pop()
            b = stack.pop()
            if n == '+':
                c = b+a
            elif n == '*':
                c = b * a
            stack.append(c)
    print('#{} '.format(1), end='')
    print(*stack)
