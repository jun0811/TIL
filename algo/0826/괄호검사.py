def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            if len(stack)== 0:
                return 1
            else:
                print(stack.pop())

arr = '()()(((())))'
stack= [ ]
print(check(arr))