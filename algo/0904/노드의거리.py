#노드의 거리 
def bfs(s):
    Q.append(s)
    visit[s] = 1
    while Q:
        v = Q.pop(0)
        if v == Goal:
            return
        for idx in line[v]:
            if not visit[idx]:
                Q.append(idx)
                visit[idx] = visit[v] + 1


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    Node = [list(map(int,input().split())) for _ in range(E)]
    Start, Goal = map(int, input().split())
    line = [[] for _ in range(V+1)]
    for a,b in Node:
        line[a].append(b)
        line[b].append(a)
    # print(line)
    Q = []
    visit = [0] * (V+1)
    bfs(Start)
    
    print('#{} {}'.format(tc, visit[Goal]-1))