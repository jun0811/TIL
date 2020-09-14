import sys
sys.stdin = open('swea1961.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    my_map = [input().split() for _ in range(N)]
    rot = []

    # 90도
    temp_lst = []
    for c in range(N):
        temp = ''
        for r in range(N):
            temp += my_map[-1 - r][c]
        temp_lst.append(temp)
    rot.append(temp_lst)

    # 180도
    temp_lst = []
    for r in range(N):
        temp = ''
        for c in range(N):
            temp += my_map[-1 - r][-1 - c]
        temp_lst.append(temp)
    rot.append(temp_lst)

    # 270도
    temp_lst = []
    for c in range(N):
        temp = ''
        for r in range(N):
            temp += my_map[r][-1 - c]
        temp_lst.append(temp)
    rot.append(temp_lst)

    # 출력
    print('#{}'.format(test_case))
    for i in range(N):
        print(rot[0][i], rot[1][i], rot[2][i])
