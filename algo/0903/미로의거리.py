

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(s_y,s_x):
    Q.append([s_y,s_x])
    visit[s_y][s_x] = 1
    global result
    while Q:
        # delQueue
        s_y , s_x = Q.pop(0)
        # print(s_y,s_x)

        for k in range(4):
            d_y, d_x = s_y + dy[k] , s_x + dx[k]
            # check = miro[d_y][d_x]
            if (0 <= d_x<N) and (0<=d_y<N) and (visit[d_y][d_x]== 0) and miro[d_y][d_x] != 1:
                # print(d_y , d_x)
                Q.append([d_y,d_x]) # 길을 찾으면 집어넣는다.
                visit[d_y][d_x] = 1
                dis[d_y][d_x] = dis[s_y][s_x] + 1 #1씩 증가하게..
                if miro[d_y][d_x] == 3: # 흠... 뭘해야하지...거리를 알아야하니깐......
                    result = dis[d_y][d_x] -1
                    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    # print(miro)
    visit = [[0]*(N) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if miro[y][x] == 2:
                s_x,s_y = x,y
    Q = [ ]
    dis = [[0]*N for _ in range(N)] #거리를 저장하자...
    result = 0
    bfs(s_y,s_x)
    # print(visit)
    print('#{} {}'.format(tc, result))
