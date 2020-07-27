
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    differ = 0
    total = 0
    for i in numbers:
        idx = numbers.index(i)  # 현재 위치 등록
        print(idx)
        for j in range(idx+1, len(numbers)+1): #최대 이득 
            print(numbers[j])
            max_gain = numbers[j] - i if numbers[j] - i > differ else differ 
        total += max_gain
    print(f'#{T} totol')
