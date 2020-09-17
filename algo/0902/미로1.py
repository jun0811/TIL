def bfs(i,j):
    #1 큐생성
    #2 시작점 enq
    #3 방문표시배열 v 생성
    #4 q가 비어있지 않으면 반복
    #5 i,j 디큐 (i,j 칸 방문)
    #6 목적지 확인, 목적지면 리턴 1
    #7 i,j에 인접인 ni,nj를 찾으면 (인접: 벽이 아니고 방문전)
    #8 ni,nj 인큐 및 방문표시
    #9 목적지에 도착하지 못하면 리턴 0
    # 1~ 3
    Q=[]
    Q.append((i,j))
    visited=[[0]*16 for _ in range(16)]
    visited[i][j]=1
 
    # 4
    while Q:
        # 5
        i,j=Q.pop(0)
        # 6
        if maze[i][j]=='3':
            return 1
        # 7
        for di,dj in[(0,1),(1,0),(0,-1),(-1,0)]:
            ni,nj = i+di,j+dj
            if maze[ni][nj]!='1' and visited[ni][nj]==0:
                # 8
                Q.append((ni,nj))
                visited[ni][nj]=visited[ni][nj]+1
    # 9
    return 0
 
## 이거 만들어놓으면 2중 for문 쉽게 빠져나옴 굿굿굿!
def find(): # 시작위치를 찾는 함수
    for i in range(16):
        for j in range(16):
            if maze[i][j]=='2':
                return bfs(i,j) # 시작위치부터 bfs 탐색
 
for _ in range(1,11):
    tc = int(input())
    maze = [input() for _ in range(16)]
    print(f'#{tc} {find()}')