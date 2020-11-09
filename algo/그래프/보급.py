from queue import PriorityQueue
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 T = int(input())
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    D = [[0xffff]*N for _ in range(N)]
    D[0][0] = MAP[0][0]
 
    q = PriorityQueue()
    q.put((D[0][0], 0, 0))
 
    while not q.empty():
        d, x, y = q.get()
        if d > D[x][y]: continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if D[nx][ny] > D[x][y] + MAP[nx][ny]:
                    D[nx][ny] = D[x][y] + MAP[nx][ny]
                    q.put((D[nx][ny], nx, ny))
    print('#{} {}'.format(t, D[N-1][N-1]))