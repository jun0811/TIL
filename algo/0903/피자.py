import sys
sys.stdin = open('input.txt')

def remain():
    i = 0
    while Q:
        if len(Q) == 1: # 마지막 하나 남았을 때
            return Q.pop(0)
        Q[0][1] //= 2
        if Q[0][1] == 0:
            if N + i < M: # 피자가 아직 남았을 때..
                Q.pop(0)
                Q.append([N+i, cheese[N+i]])
                i += 1
            else: # 더이상 피자가 뒤에 없으때 걍 보내야 한다.
                Q.pop(0)
        else:
            Q.append(Q.pop(0))
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # N: 화덕 크기 (Q길이)/ M: 피자갯수
    cheese = list(map(int, input().split()))
    # 치즈는 한바퀴(N)움질일 때마다 치즈가 반씩 녹는다.
    # 마지막 남아있는 피자
    Q = []
    for i in range(N): #피자 인덱스랑 치즈양 한번에 다루기
        Q.append([i ,cheese[i]])
    # print(Q)
    result = remain()
    print('#{} {}'.format(tc, result[0]+1))