# 미로 풀기 #4875
# recursive와 스택 이용차이 
'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''
import sys
sys.stdin = open('input.txt')
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y,x):
    s = []
    s.append([y,x])
    visted[y][x] = 1
    
def dfsr(y,x):
    miro[y][x] = -1
    for i in range(4):
        newX = x +dx[i]
        newY = y +dy[i]
        # print(newY,newX)
        if newY<0 or newY>=N or newX>=N or newX<0:
            continue
        if miro[newY][newX] == 3:
            return 1
        if miro[newY][newX] != 1 and miro[newY][newX] == 0:
            if dfsr(newY,newX) == 1:
                return 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # miro = [list(input()) for _ in range(N)]
    miro = [[int(x) for x in input()] for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    
    for j in range(N):
        for i in range(N):
            if miro[j][i] ==3:
                f_y, f_x = j,i
                # print(1)
            if miro[j][i]==2:
                s_y,s_x = j,i 
                # print(1)

    result = dfsr(s_y,s_x)
    if result:
        print(1)
    else:
        print(0)

