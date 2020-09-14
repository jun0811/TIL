# import sys
# sys.stdin = open('sample_input.txt')
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def search(j,i,goal_y,goal_x):
    visited[j][i] =1
    y, x = j,i
    if goal_y ==j and goal_x==i:
        return

    for k in range(4):
        x += dx[k]
        y += dy[k]
        if 0<= x <N and 0<= y < N and (not visited[y][x]) and (miro[y][x] =='0' or '3'):
            search(y,x,goal_y,goal_x)
        y = j
        x = i
for tc in range(1,T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if miro[j][i] == '3':
                f_y, f_x = j,i
    
    for j in range(N):
        for i in range(N):
            if miro[j][i] == '2':
                search(j,i,f_y,f_x)

    if visited[f_y][f_x] == 1:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))

