import sys
sys.stdin=open('ladder2.txt','r')

for t in range(10):
    T = int(input())
    box = [list(map(int,input().split())) for _ in range(100)]


    ladder = [ ]
    for i in range(100):
        if box[0][i] ==1:
            ladder.append(i)

    min_cnt = 10000
    check = 0
    for j in range(len(ladder)):
        flag = ladder[j]
        start = flag
        cnt = 0
        for i in range(100):
            if (flag-1 >=0) and box[i][flag-1] ==1:
                while (flag -1 >=0 ) and box[i][flag-1] ==1:
                    flag -= 1 
                    cnt += 1                   
            elif (flag+1<=99) and box[i][flag+1]==1:
                while (flag +1<=99) and box[i][flag+1] ==1:
                    flag += 1
                    cnt += 1
            cnt += 1
        if min_cnt > cnt :
            min_cnt = cnt
            check = start
        
    print('#{} {}'.format(T, check ))

####

for t in range(10):
    T = int(input())
    box = [list(map(int,input().split())) for _ in range(100)]


    ladder = [ ]
    for i in range(100):
        if box[0][i] ==1:
            ladder.append(i)

    min_cnt = 10000
    check = 0
    for j in range(len(ladder)):
        flag = ladder[j]
        start = flag
        cnt = 0
        for i in range(100):
            if flag > 0 and box[i][flag-1] ==1:
                cnt += ladder[j] - ladder[j-1]
                j -= 1
                flag = ladder[j]
            elif flag < 99 and box[i][flag+1]==1:
                cnt += ladder[j+1] - ladder[j]
                j += 1
                flag = ladder[j]
        if cnt < min_cnt:
            min_cnt = cnt
            check = start
            # print(start)
    print('#{} {}'.format(T, check))
    