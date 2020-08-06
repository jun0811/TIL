# 부분 집합 구하기

'''
123 = 1*(10^2) + 2*(10^1) + 3 * (10^0)

101 => 1*(2^2) + 1*(2^0) = 5


arr = [1 , 2, 3, 4, 5]  
# 00000 ~ 11111 -> 0 ~31 
[0 0 0 0 0]  2진법 : 00000
[1 0 0 0 0]  2진법 : 00001
    
     .....

'''
# arr = list(map(int, input().split()))

# for i in range(1<<len(arr)):
#     # i(00000.. -> 11111..) 이용
#     # 101 & 001 -> 001 // 101 & 010 -> 2번째 bit 쳌 0
#     #      (1<<0)               (1<<1)
#     total = 0
#     # i  = 000 001 010 011 100 101 110 111
#     for j in range(len(arr)): #체크 해야할 인자들
#         # j = 0 1 2 
#         if i & 1<<j:
#             print('i:', i)
#             print('j:', j)
#             total += arr[j]
    
#     if total == -1:        
#         print(True)

arr = list(map(int, input().split()))

for i in range(1<<len(arr)):
    # i(00000.. -> 11111..) 이용
    # 101 & 001 -> 001 // 101 & 010 -> 2번째 bit 쳌 0
    #      (1<<0)               (1<<1)
    # i  = 000 001 010 011 100 101 110 111
    temp =[]
    for j in range(len(arr)): #체크 해야할 인자들
        # j = 0 1 2
        if i & 1<<j:
            print(i , j)
            temp.append(arr[j])
    print(temp)


