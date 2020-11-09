def mul(n):
    return n*2

# 값이 바뀌고 그걸 넘기고 다시 4개 경우의 수 다시 보고 
def bfs(s,cnt):
    global min_cnt

    if (cnt >= min_cnt):
        return

    for c in cal:
        if c==2:
            n = mul(s)

            if n ==M:
                if cnt+1 < min_cnt:
                    min_cnt = cnt+1
                return
            bfs(n,cnt+1)
        s += c
        if s >= 1000000 or (s < 1):
            s -= c
            continue
        if s == M:
            if cnt+1 < min_cnt:
                min_cnt = cnt+1
            return
        bfs(s,cnt+1)
        s -= c



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    # 1, -1, *2, -10
    cal = [1,-1,2,-10]
    visited = [0]*4
    min_cnt = 0XFFFF 
    bfs(N,0)
    print('#{} {}'.format(tc,min_cnt))