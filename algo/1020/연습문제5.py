import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    K = int(input()) # 자석 회전수
    N, M = map(int,input().split()) # 자석수, 칼날 수  
    mag = [list(map(int, input().split())) for _ in range(N)]
    # print(mag)
    for _ in range(K):
        idx, rot = map(int, input().split())
        # print(idx, rot)
        idx -= 1  # 0 ~ N-1번 톱니
        move = [(idx, rot)]  # 돌릴 톱니

        # 왼쪽 톱니 확인
        temp = rot
        for i in range(idx - 1, -1, -1):
            if mag[i][1] != mag[i + 1][M-2]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        # 오른쪽 톱니 확인
        temp = rot
        for i in range(idx + 1, N):
            if mag[i][M-2] != mag[i - 1][1]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        # 톱니 돌림
        for idx, rot in move:
            if rot == 1:
                mag[idx] = [mag[idx].pop()] + mag[idx]
            elif rot == -1:
                mag[idx].append(mag[idx].pop(0))

    # 결과 계산
    result = 0
    for i in range(N):
        result += mag[i][0] * 2**i

    print('#{} {}'.format(test_case, result))