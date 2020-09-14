# import sys
# sys.stdin = open('input.txt','r')
dy = [0,0,1,-1]
dx = [1,-1,0,0]
T = int(input())
for tc in range(1, T+1):
    square = [list(input().split()) for _ in range(4)]
    Q = []
    result = []
    #각 자리마다 만들 수 있는 수...각자리 체크
    for y in range(4):
        for x in range(4):
            # print(y, x)
            Q.append([y,x,0, square[y][x]])
            while Q:
                y, x, count, total = Q.pop()
                if count >= 6:
                    result.append(total)
                    continue
                for k in range(4):
                    d_y = y + dy[k]
                    d_x = x + dx[k]
                    if 0<= d_y <4 and 0<= d_x < 4:
                        Q.append([d_y,d_x,count+1,total + square[d_y][d_x]])
    print('#{} {}'.format(tc, len(set(result))))