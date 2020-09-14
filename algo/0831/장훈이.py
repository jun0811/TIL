

def f1(n,g,k,m): #n 고려할 직원넘버, g 직원수 ,k 는 선반높이, m  n-1번가지 만들어진 탑의 높이
    
    if n == g: # 모든 직원이 고려된 경우
        if m >= k and minV > m-k:
            minV = m
    elif m>=k and minV <= m-k: #r고려할직원이 남아잇지만 기존보다 크다면


    else:
        f(n+1, g, k, m) # n 번 탑에 참여하지 않음.(이전 직원 까지의 높이 m이 그래도 유지)
        f(n+1, g, k, m+H[n]) #  n-1가지의 높이 m+H[n] n번 직원의 높이




def f(n, g, k): #n 고려할 직원넘버, g 직원수
    global minV
    if n == g: # 모든직원에 대해 고려
        s = 0
        print(A)
        for i in range(g):
            if A[i]: #참여하는 경우
                s += H[i] # 키를 더함
        if k <= s and s-k < minV: #키 합이 선반 이상이고, 차이가 최소이면
            minV = s-k


    else:
        A[n] = 0 # n번직원 미참여
        f(n+1, g, k) # n+1번 직원 결정하러 이동
        A[n] = 1 #n번직원 참여
        f(n+1, g, k)


T = int(input())
for tc in range(1,T+1):
    N,K = ma[(int, input().split())]
    H = list(map(int, input().split()))
    A = [0]*N #탑에 포함되있는디 표시
    minV = 100000000 #대충큰값
    f(0, N, K) 
