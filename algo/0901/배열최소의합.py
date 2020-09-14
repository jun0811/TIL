import sys
sys.stdin = open('sample_input.txt')

def find(x):
    global temp, minV
    if minV < temp: # 다 돌기전에 기존의 값보다 클 수 있다.
        return # 할필요 없음
    elif x == N: 
        if temp < minV:
            minV = temp
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            temp += square[x][i]
            find(x+1)
            visited[i] = 0
            temp -= square[x][i] # 더 햇던 값을 빼서 초기화
 

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # N X N 행렬
    square = [list(map(int, input().split())) for _ in range(N)]
    temp = 0
    minV = 100000
    visited = [0] * N
    find(0)
    print('#{} {}'.format(tc, minV))