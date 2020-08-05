# 4방향 검색  // 벽을 만나면 ...? // 
'''
제일 작은 걸 뽑고 그다음 것보다 큰거 
'''
def getMin(curV):
    minV = 1000000
    for i in range(5):
        for j in range(5):
            if minV> src[i][j]:
                minV = src[i][j]
    return 


def isWall(x,y):
    #진짜 벽과 값이 있는 벽 처리 
    if x<0 or x>=5:
        return False
    if y<0 or x>=5:
        return False
    if dst[y][x] != 0:
        return False

    return True

dst = [[0]*5 for _ in range(5)]

src = list(map(int,input().split()))

curX = curY = 0
curV = 
dx = [1,0,-1,0] 
dy = [0,1,0,-1]
dir = 0 
for i in range(25):
    val = getMin(src)
    dst[curY][curX] = val
    testX = curX + dx[dir]
    testY = curY + dy[dir]
    if isWall(testX,testY):

    