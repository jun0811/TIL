for test_case in range(1,11):
    i = int(input())
    
    second_arr = [list(map(int,input().split())) for _ in range(100)]
    
    seek_max = []
    line_sum = 0
    cross = 0
    #가로
    for i in range(100):
        for j in range(100):
            line_sum += second_arr[i][j]
            if i == j:
                cross += second_arr[i][j]
        seek_max.append(line_sum)
        line_sum = 0
    
    #세로
    for j in range(100):
        for i in range(100):
            line_sum += second_arr[i][j]
        seek_max.append(line_sum)
        line_sum = 0
    
    seek_max.append(cross)
    print(max(seek_max))
    