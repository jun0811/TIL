def postord(T):
    if T:
        postord(int(tree[T][2]))
        postord(int(tree[T][3]))
        if tree[T][1] not in ['+', '-', '*', '/']:
            S.append(tree[T][1])
        else:
            n1 = S.pop()
            n2 = S.pop()
            if tree[T][1] == '+':
                S.append(int(n2)+int(n1))
            if tree[T][1] == '-':
                S.append(int(n2)-int(n1))
            if tree[T][1] == '*':
                S.append(int(n2)*int(n1))
            if tree[T][1] == '/':
                S.append(int(n2)//int(n1))
 
 
for tc in range(1, 11):
    N = int(input())
    tree = [[0]*4]+[list(input().split()) for _ in range(N)]
    S = []
    for t in tree:
        while len(t) < 4:
            t.append(0)
    postord(1)
    print('#{} {}' .format(tc, S[0]))