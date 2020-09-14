# https://www.acmicpc.net/problem/1012
import sys

sys.setrecursionlimit(100000)
dx = [1,0,0,-1] # 오 위 아래 
dy = [0,-1,1,0]

def dfs(j,i):
    global cnt
    visited[j][i] = 1 # 방문 했으므로 1로 바꿔주기
    for k in range(4): # 방문하고 사방을 체크 
        d_x = i + dx[k]
        d_y = j + dy[k]
        if 0<=d_x<M and 0 <= d_y <N and (not visited[d_y][d_x]) and (farm[d_y][d_x]==1) :
                dfs(d_y,d_x)



T = int(input())
for i in range(1,T+1):
    M, N, K = map(int,input().split())
    farm = [[0]*M for _ in range(N)] 
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y  = map(int,input().split())
        farm[Y][X] = 1
    for j in range(N):
        for i in range(M):
            if (visited[j][i]==0) and (farm[j][i] == 1): # 해당 인덱스가 0이면
                dfs(j, i)
                cnt += 1
    print(cnt)
    
