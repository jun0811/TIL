import sys
sys.stdin = open('input.txt')

dx = [0,1,0,-1]
dy = [1,0,-1,0]
 
T = int(input())
for t in range(T):
    N = int(input())
    square=[]
    max_cnt = 0 # 결과
    start = 0
    for _ in range(N):
        square.append(list(map(int,input().split())))
    for x in range(N): # 모든 x,y 탐색
        for y in range(N):
            cnt = 1 
            q = [(x,y)] # 첫 시작 
            while q: # BFS 탐색 
                a,b = q.pop()
                for i in range(4):
                    if 0 <= a + dx[i] < N and 0 <= b + dy[i] < N and (square[a+dx[i]][b+dy[i]] - square[a][b] == 1):
                        cnt += 1
                        q.append((a+dx[i],b+dy[i]))
            if cnt > max_cnt:
                max_cnt = cnt 
                start = square[x][y] 
            elif cnt == max_cnt: # 건너온 개수가 같다면
                if square[x][y] < start: 
                    start = square[x][y]
 
    print('#{} {} {}'.format(t+1,start, max_cnt))