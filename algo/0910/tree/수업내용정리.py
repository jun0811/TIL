# 수업내용 정리

# 선형구조, 비선형구조

# 선형구조(1:1 관계)
# 표현 방법 : list
# 순회 : for문

# 비선형구조
# 트리(1:N) ,그래프(N:N)
# 포함관계  -  그래프 > 트리 > 이진트리


# 표현방법 (저장)
# 그래프(N:N) : 인접행렬, 인접리스트, 간선배열
# 이진트리(1:N) : 1차원 배열, 1차원배열(인접리스트)

# 순회방법
# 그래프(N:N) : DFS(stack), BFS(Queue)       -  A형 평가 주 내용
# 이진트리(1:N) : 전위순회, 중위 순회, 후위 순회 (visited 체크 안해도 됨)
# 선형구조 : 완전검색, 가지치기 (재귀: 부분집합, 순열, 조합)   - IM형 평가 주 내용

# DFS 복습
# 스토리를 기억할 것
# 1. 시작과 동시에 방문체크
# 2. 인접행렬에서 자신의 열에 있는 (즉, 연결되어있는 노드확인)
# 3. 각 노드가 1이고 방문하지 않았으면 dfs방문
# 주의: 재귀로 만들 때 항상 stack overflow를 고민을 해야함(1000개까지만 가능)
def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

G = 인접행렬(2차원배열)
visited = [0] * N
dfs(1)

# BFS 복습(둘다 가능하다면 BFS가 DFS보다 낫다(stack overflow))

def bfs(v):
    q = []
    q.append(v)      # enQueue : 방문처리
    visited[v] = 1
    print(v, end=' ')
    while q:
        v = q.pop(0)      # deQueue 
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
                pritn(w, end=' ')

G = 인접리스트(2차원)
visited = [0] * N

bfs(시작지점)



