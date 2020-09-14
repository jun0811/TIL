import sys
sys.stdin = open("input.txt", "r")

def check(arr, i, j):
    result = 0
    for m in range(N-1, -1, -1):
        
        if arr[i][j:j+m+1] == arr[i][j:j+m+1][::-1]:
            pal = len(arr[i][j:j+m+1])
            return pal

N = 100
for _ in range(10):
    T = int(input())
    BRD = [list(input()) for _ in range(N)]
    trans = list(map(list, zip(*BRD)))

    # 가로
    ans = 0
    length = 0
    for i in range(N):
        for j in range(N):
            length = check(BRD, i, j)

    # 세로
    ans = 0
    length = 0
    for i in range(N):
        for j in range(N):
            length = check(trans, i, j)
            if length > ans:
                ans = length

    print('#{} {}'.format(T, ans))