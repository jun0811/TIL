T = int(input())

for TC in range(1, T + 1):
    N = int(input()) //10
    dp = []
    dp.append(1)
    dp.append(3)
    for i in range(2,N):
        num = dp[i-1] + dp[i-2] * 2
        dp.append(num)

    print("#{} {}".format(TC, dp[-1]))