import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    # 1 -> N극 성질 // 2 -> S극 성질 1을 밑으로 쭉쭉 , 2는 위로 쭉쭉
    # 같은 렬에만 없으면 되는군...
    stack = [ ]
    inter = 0
    for x in range(100):
        for y in range(100): # 위로 
            if table[y][x] == 1:
                stack.append(1)
            elif len(stack) > 0 and (table[y][x] == 2):
                    stack = []
                    inter += 1
        stack = []
    print('#{} {}'.format(tc,inter))
