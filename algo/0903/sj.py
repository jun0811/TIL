import sys
sys.stdin = open("input.txt", "r")

def solution():
    i = 0
    while len(pizza) != 1:
        if len(pizza) == 1:
            return
        n, cheese = pizza.pop(0)
        if cheese == 0:
            if N + i < M:
                pizza.append(tmp[N+i])
                i += 1
        elif cheese != 0:
            pizza.append((n, cheese // 2))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    Ci = list(map(int, input().split()))

    tmp = []
    for i in range(M):
        tmp.append((i+1, Ci[i]))
    pizza = tmp[:N]


    solution()
    print(pizza[0][0])