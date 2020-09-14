# 흐름 
# 큐 생성
# 시작점
# 방분 표시 -> visit 
# 인접 리스트 , delta 검색 인자
import sys
sys.stdin = open('input.txt')



def bfs(j,i):
    Q = []
    visited = [[0]*16 for _ in range(16)]
    Q.append([j,i])
    visited[j][i] = 1
    while Q:
        dy, dx = Q.pop(0)
        if maze[dy][dx] == '3':
            return 1
        for a, b in [[0,1], [1,0], [0,-1],[-1,0]]:  
            d_y, d_x = dy + a, dx + b # 델타 검색 
            if (visited[d_y][d_x] == 0) and (maze[d_y][d_x] !='1'):
                Q.append([d_y,d_x])
                visited[d_y][d_x] = visited[dy][dx] + 1 
    return 0


for _ in range(1,11):
    tc = int(input())
    maze = [input() for _ in range(16)]
    for y in range(16):
        for x in range(16):
            if maze[y][x] == '2':
                result = bfs(y,x)
    
    print('#{} {}'.format(tc,result))