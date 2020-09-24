import sys

sys.stdin = open('빙고.txt')

def find(n):
    for y in range(5):
        for x in range(5):
            if bingo[y][x] == n:
                bingo[y][x] = 0

def check():
    success = 0
    c = 0 # 세로검사
    r = 0 # 오른쪽밑 대각선 
    l = 0 # 왼쪽밑 대각선 
    for y in range(5):
        if bingo[y].count(0) == 5:
            success +=1
        
        for x in range(5):
            if (y==0) and (bingo[y][x]==0):
                c+=1
        if c==5:
            success+=1
        if bingo[y][y] == 0:
            r += 1
        if  bingo[y][4-y] == 0:
            l += 1
    if r==5:
        success += 1
    if l==5:
        success += 1 
    return success 

bingo = [list(map(int,input().split())) for _ in range(5)]

number = [list(map(int,input().split())) for _ in range(5)]
# 적어도 12개는 불러야 빙고가 나올수잇음

cnt = 0
ans= 0
for y in range(5):
    for x in range(5):
        find(number[y][x])
        cnt += 1
        if cnt>=12:
            if check() >= 3:
                ans = cnt
                break
    if ans>0 :
        break
print(ans)

print(cnt)