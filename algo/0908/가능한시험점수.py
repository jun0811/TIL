
# def p_set(n,midV):
#     global temp
#     if n == N:
#         used[midV] = 1
#     else:
#         temp += score[n]
#         p_set(n+1, temp)
#         temp -= score[n]
#         p_set(n+1, temp)
            
        
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
 
    maxV = sum(score)
    used = [0] * (maxV + 1)
 
    S = [0]
    for num in score:
        t = len(S)
        for j in range(t):
            if not used[S[j] + num]:
                S.append(S[j] + num)
                used[S[j]+num] = 1
 
    print('#{} {}'.format(tc, len(S)))
    # 1 = >2  | 2=>4 | ...데이터가 너무 많으면 위와같은 경우의 수를 이용 