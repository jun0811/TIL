def P_set(n,k): 
    global minV
    if n == k:
        result = 0
        for i in range(n):
            if visit[i] == 1:
                result += S[i]
        tmp = result - B # 내 값 - 선반 높이 차가 양수이고 제일 작으면 저장
        if tmp >= 0 and minV >tmp:
            minV = tmp

    else:
        visit[k] = 1 
        P_set(n,k+1)
        visit[k] = 0
        P_set(n,k+1)



T = int(input())

for tc in range(1,T+1):
    N,B = map(int,input().split())
    S = list(map(int,input().split()))
    minV = float('inf')
    visit = [0] * N
    P_set(N,0)
    print('#{} {}'.format(tc,minV))