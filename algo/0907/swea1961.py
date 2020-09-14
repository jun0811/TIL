def rotation(nums):
    tmp = [['']*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            #회전하는 함수
            tmp[j][N-1-i] = nums[i][j]
    return tmp

def result(nums, col):
    for i in range(N):
        for j in range(N):
            ans[i][col] += nums[i][j]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    ans = [[''] * 3 for _ in range(N)]
    #90도를 3번 돌린다.
    for i in range(3):
        arr = rotation(arr)
        result(arr, i)

    print("#{}".format(tc))
    for i in range(N):
        for j in range(3):
            print(ans[i][j], end= " ")
        print()