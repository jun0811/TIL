# 10 x 10 이중 리스트에서 
# 빨강색 만큼 1을 대입
# 파랑색에 -1을 대입 
# 합이 0



def colar(x1,y1,x2,y2,c, a):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            if c==1:
                a[y][x] += 1
            if c==2:
                a[y][x] += 2


T = int(input())

for test_case in range(1,T+1):
    square = [[0]*10 for _ in range(10)]

    N = int(input())
    ss = []
    for i in range(N):
        s = list(map(int,input().split()))
        ss.append(s)

    #print(ss)

    for s in ss:
        colar(s[0],s[1],s[2],s[3],s[4], square)

    #print(square)
    
    cnt =0
    for y in range(10):
        for x in range(10):
            if square[y][x] == 3:
                cnt +=1

    print('#{} {}'.format(test_case, cnt))