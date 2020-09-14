dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def check(p_x,p_y,stone):

    
    for i in range(8):
        d_x, d_y = p_x, p_y
        d_x += dx[i]
        d_y += dy[i]
        cnt = 0

        while visted[d_y][d_x] != stone:
            if visted[d_y][d_x] == 0:
                cnt = 0
                break
            else:
                cnt += 1
                d_x += dx[i]
                d_y += dy[i]
        d_x, d_y = p_x, p_y
        for _ in range(cnt):
            d_x += dx[i]
            d_y += dy[i]
            visted[d_y][d_x] = stone

T  = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    # 1이면 흑돌 2이면 백돌
    point = []  # 돌들의 좌표가 담길 리스트 
    visted =[list([0]*(N+2)) for _ in range(N+2)]
    init_pos = N//2
    visted[init_pos+1][init_pos+1] = 2
    visted[init_pos][init_pos] = 2
    visted[init_pos][init_pos+1] = 1
    visted[init_pos+1][init_pos] = 1

    for _ in range(M):
        x, y, stone = map(int, input().split())
        visted[y][x] = stone
        check(x,y,stone) # 스톤 데이터 처리 

    B,W= 0, 0

    for v in visted:
        B += v.count(1)
        W += v.count(2)
    print('#{} {} {}'.format(tc, B, W))