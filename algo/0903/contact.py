# import sys
# sys.stdin = open('input.txt')
def bfs(v): #
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1 #거리 증가


for tc in range(1,11):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    end = max(numbers)
    G = [[] for _ in range(end+1)] 
    for i in range(0,len(numbers)//2):
        a, b = numbers[i*2], numbers[i*2 + 1] # 인접 리스트 시작->끝 
        G[a].append(b)
    # print(G)
    visited = [0] * (end + 1 ) # 방문 여부 
    bfs(M)
    result = max(visited)
    visited.reverse() 
    # 맨뒤에 있을 가장 큰 값을 쉽게 찾기 위해
    print('#{} '.format(tc), end= '')
    print(len(visited) - visited.index(result)- 1)