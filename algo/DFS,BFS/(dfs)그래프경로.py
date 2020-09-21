import sys
sys.stdin = open('sample_input.txt')

def bfs(v):
    visited[v] = 1
    if v == G :
        return
    for i in line[v]:
        if not visited[i]:
            bfs(i)


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    visited = [0] *(V+1)
    line = [[] for _ in range(V+1)] 
    for i in range(E):
        a, b = map(int, input().split())
        line[a].append(b)
    S,G = map(int, input().split())
    bfs(S)
    if visited[G]:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))