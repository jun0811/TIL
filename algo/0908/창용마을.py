import sys
sys.stdin = open('input.txt')

def dfs(n):
    visited[n] = 1
    for i in R[n]:
        if not visited[i]:
            dfs(i)
        


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # 사람 수, 사람관계
    P = [list(map(int,input().split())) for _ in range(M)]
    R = [[] for _ in range(N+1)] #누가 누구와 
    for a, b in P:
        R[a].append(b)
        R[b].append(a)
    # print(R)
    cnt = 0 # 그룹 수 
    visited = [0] * (N+1) # 0번이 1번
    # 한번도 들리지 않은 인덱스를 찾아서 dfs 검색
    for i in range(1,N+1):
        if visited[i] == 0:
            dfs(i) # 사람의 그룹찾기
            cnt+=1
    print('#{} {}'.format(tc, cnt))