def width(i,j):
    count = 1
    dx = j
    while True:
        dx += 1
        if dx >= N:
            break
        if square[i][dx]:
            count += 1
        else:
            break
    return count

def height(i,j):
    count = 1
    dy = i
    while True:
        dy += 1
        if dy >= N:
            break
        if square[dy][j]:
            count += 1
        else:
            break
    return count


def change(y1,x1,y2,x2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            square[i][j] = 0


T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    # 행렬값을 입력받고 -> 행렬조사를 시작 
    # x 축으로 진행하다가 벽(0)을 만나면 y축으로 진행, 진행하다가 0을만나면 값저장 행렬 크기 
    # y축 
    square = [list(map(int, input().split())) for _ in range(N)]
    
    result = []
    row = 0
    colum = 0 
    for y in range(N):
        for x in range(N):
            if square[y][x]:
                w = width(y,x)
                h = height(y,x)
                #print(w, h)
                change(y,x, y+h, x+w)
                result.append([h, w, h*w])
    result = sorted(result, key = lambda x:(x[2],x[0]))
    temp = []
    for i in result:
        temp.append(str(i[0]))
        temp.append(str(i[1]))
    print('#{} {} {}'.format(test_case, len(result), ' '.join(temp)))
    
                