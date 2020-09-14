

def bfs(v, goal):
    Q = []
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] +1 # 거리당 1씩
                if w == goal:
                    return

T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())
    visited = [0] * (V+1)
    G = [[] for _ in range(0,V+1)]
    lines = [list(map(int,input().split())) for i in range(E)]
    # print(lines)
    for i in range(E): # 양쪽 노드 서로 연결
        a, b = lines[i][0], lines[i][1]
        G[a].append(b)
        G[b].append(a)
    S, E = map(int, input().split())
    bfs(S,E)
    # print(G)
    # print(visited)
    distance = visited[E] - visited[S]
    if visited[E]:
        print('#{} {}'.format(tc, distance))
    else:
        print('#{} 0'.format(tc))