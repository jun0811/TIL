for t in range(10):
    T = int(input())
    box = [list(map(int,input().split())) for _ in range(100)]

    for i in range(100):
        if box[99][i] == 2 :
            flag = i 

    ladder = [ ]
    for i in range(100):
        if box[0][i] ==1:
            ladder.append(i)

    for i 

    
    for i in range(99,-1 ,-1):
        if (flag-1 >=0) and box[i][flag-1] ==1:
            while (flag -1 >=0 ) and box[i][flag-1] ==1:
                flag -=1 
        elif (flag+1<=99) and box[i][flag+1]==1:
            while box[i][flag+1] ==1 and (flag +1<=99) :
                flag += 1





    print('#{} {}'.format(T, flag))

        # for i in range(100):
    #     if box[0][i] == 1:
    #         ladder.append(i)

    # L = ladder.index(flag)

    # for i in range(100):
    #     if box[99-i][flag-1] == 1:
    #         flag = ladder[L-1]
    #         L -= 1 
    #     elif box[99-i][flag+1] == 1:
    #         flag = ladder[L+1]
    #         L +=1
    #####################
    #####################
    # for tc in range(1, 11):
    # N = int(input())
    # arr = [0] * 100
    # for i in range(100):
    #     arr[i] = list(map(int, input().split()))
 
 
    # goal = []
    # for x in range(99, 100):
    #     for y in range(100):
    #         if arr[x][y] == 2:
    #             goal.append(y)
 
 
    # dx = [-1, 0, 0]
    # dy = [0, -1, 1]
 
    # answer = 0
    # for g in goal:
    #     nx = 99
    #     ny = g
 
    #     while nx > 0:
 
 
    #         ans = {}
    #         for k in range(3):
    #             nnx = nx + dx[k]
    #             nny = ny + dy[k]
    #             if 0<= nnx < 100 and 0 <= nny < 100:
    #                 if arr[nnx][nny] == 1:
    #                     ans[k] = [nnx, nny]
    #                     arr[nnx][nny] = 0
 
    #         if ans.get(1):
    #             nx = ans[1][0]
    #             ny = ans[1][1]
    #         elif ans.get(2):
    #             nx = ans[2][0]
    #             ny = ans[2][1]
    #         else:
    #             nx = ans[0][0]
    #             ny = ans[0][1]
 
    #         if nx == 0:
    #             answer = ny
 
    #     print('#{}'.format(tc), answer)