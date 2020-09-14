# https://www.acmicpc.net/problem/2667
# import sys
# sys.stdin = open('a.txt','r')
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y, x, t):
    visited[y][x] = t 
    for k in range(4):
        d_x = x + dx[k]
        d_y = y + dy[k]
        if (0<=d_x<N) and (0<= d_y < N) and not visited[d_y][d_x] and (apt[d_y][d_x] ==1):
            dfs(d_y,d_x,t)
            
            
N = int(input())
visited = [[0]*N for _ in range(N)]
apt = []
total =[]
for i in range(N):
    apt.append(list(map(int,input())))
t = 0

for j in range(N):
    for i in range(N):
        if (visited[j][i]==0) and (apt[j][i] == 1):
            t += 1
            dfs(j,i,t)
            
print(t)
for i in range(1,t+1):
    cnt = 0
    for v in visited:
        cnt += v.count(i)
    total.append(cnt)
total.sort()
for t in total:
    print(t)
            
