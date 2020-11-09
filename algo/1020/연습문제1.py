# 이중for문
dy = [1,-1,0,0]
dx = [0,0,-1,1]

N= 5


arr = []
s = 1
for _ in range(N):
    a = []
    for _ in range(N):
        a.append(s)
        s+=1
    arr.append(a)

print(arr)
    

total = 0
for j in range(N):
    for i in range(N):
        for k in range(4):
            newY = j +dy[k]
            newX = i +dx[k]
            if newY>=0 and (newX>=0) and (newY<N) and (newX<N):
                total += abs(arr[j][i] - arr[newY][newX])
                # print(arr[y][x], '||' ,arr[newY][newX])
print(total)