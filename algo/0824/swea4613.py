# 접근 방법 
# 칠해야하는 최소 칸수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj&categoryId=AWQl9TIK8qoDFAXj&categoryType=CODE&&&

import sys
sys.stdin = open('input.txt','r')
T = int(input())

for test_case in range(1,T+1):
    N,M = map(int, input().split())
    colors = [input() for _ in range(N)]
    # print(colors) 
    W = [0] * N # W가 아닌 것들 누적갯수
    B = [0] * N # B가 아닌 것들 누적갯수
    R = [0] * N # R가 아닌 것들 누적갯수
    i = 0 
    for color in colors:
        if i:
            W[i] += W[i-1] # 누적
            B[i] += B[i-1] 
            R[i] += R[i-1] 
        for c in color:
            if c != 'W':
                W[i] += 1
            if c != 'B':
                B[i] += 1
            if c != 'R':
                R[i] += 1
        i += 1

    minV = N*M  # 색칠 해야하는 최소 갯수 
    for i in range(N-2): # 첫 구간 i 
        for j in range(i+1,N-1): # 두 번째 구간 i+1 ~j 
            s1 = W[i]  # 처음 흰색을 몇개나 칠해야 하는지 
            s2 = B[j] -B[i] # 다음 블루를 ~
            s3 = R[N-1] - R[j] # 마지막 레드를 ~
            if minV >s1 +s2 +s3: # 최소 값 check 
                minV = s1 +s2 + s3
    print(f'#{test_case} {minV}')
