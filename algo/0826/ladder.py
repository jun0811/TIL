for t in range(10):
    T = int(input())
    box = [[0]] * 100
    for i in range(100):
        box[i] = [0] + list(map(int, input().split())) + [0]
         
    L = []
    for i in range(102):
        if box[0][i] == 1:
            L.append(i)
    flag = 0
    for i in range(102):
        if box[99][i] == 2:
            flag = i
    I = L.index(flag)
 
    for i in range(100):
        if box[99-i][flag-1] == 1: 
            flag = L[I-1]
            I -= 1
        elif box[99-i][flag+1] == 1:
            flag = L[I+1]
            I += 1
 
    print('#{} {}'.format(T,flag-1))
