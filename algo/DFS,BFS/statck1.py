T = int(input())

for tc in range(1,T+1):
    N = int(input())//10 # 가로....
    dp = []
    dp.append(1) # 가로 1
    dp.append(3) # 가로 2
    for i in range(2,N):
        num = dp[i-1] + dp[i-2] *2
        dp.append(num)
    print('#{} {}'.format(tc,dp[-1]))