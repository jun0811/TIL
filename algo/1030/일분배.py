def perm(k):
    if k == N:
        print(tr)
        res = 1
        for i in range(N):
            res = res*ARR[i][tr[i]] //100
        if maxV <res:
            maxV =res
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                tr[k] = i
                perm(k+1)
                visited[i] = False


tr = [0] *N 
ARR = 입력 배열

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]