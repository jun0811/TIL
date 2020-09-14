N = int(input())
num = list(map(int, input().split()))

com = []
for i in range(1,len(num)):   
    if num[i] - num[i-1] > 0:
        com += [1]
    elif num[i] == num[i-1]:
        com += [0]
    else:
        com += [-1]

max_num = 0
count = 0
standard = 0
for i in com:
    if i == 1:
        if standard == (0 or 1):
            count += 1
            if max_num < count:
                max_num = count
        else:
            count = 1
        standard = 1
    elif i == -1:
        if standard == (0 or -1):
            count += 1
            if max_num < count:
                max_num = count
        else:
            count = 1
        standard = -1
    else:
        count += 1
        if max_num < count:
            max_num = count

print(max_num+1)