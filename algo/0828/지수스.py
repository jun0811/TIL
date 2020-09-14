


direct = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]

def check(c):
    for a,b in test:
        table[a][b] = c


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    table = [list([0]*(N+2)) for _ in range(N+2)]
    h = int(N/2)
    table[h][h] = 2
    table[h+1][h] = 1
    table[h][h+1] = 1
    table[h+1][h+1] = 2


    for i in range(M):
        a, b, c = map(int, input().split())
        table[a][b] = c

        for i in range(8):
            x ,y = direct[i]
            test = []
            while True:
                a, b = a+x, b+y
                if table[a][b] == c:
                    check(c)
                    break
                elif table[a][b] == 0:
                    break
                else:
                    test.append([a,b])
            a,b = 
    cnt_1 = 0
    cnt_2 = 0
    for i in range(N+2):
        for j in range(N+2):
            if table[i][j] == 1:
                cnt_1 += 1
            elif table[i][j] == 2:
                cnt_2 += 2
    print(cnt_1, cnt_2)
