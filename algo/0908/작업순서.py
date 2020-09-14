import sys
sys.stdin = open('input.txt')

for tc in range(1,2):
    V, E = map(int,input().split())
    G = list(map(int, input().split()))
    visited= [[0] *(V+1) for _ in range(V+1)]
    # line = [[] for _ in range(V+1)]
    # prior = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = G[2*i], G[2*i+1]
        visited[b][a] = 1
    GOAL = []
    while True:
        if len(GOAL) == V:
            break
        start = []
        for y in range(1, len(visited)):
            if 1 not in visited[y] and y not in GOAL:
                start.append(y)

        for y in start:
            GOAL.append(y)
            for x in range(len(visited)):
                visited[x][y] = 0

    print('#{}'.format(tc), end = " ")
    for num in GOAL:
        print('{}'.format(num), end=' ')
    print('')
