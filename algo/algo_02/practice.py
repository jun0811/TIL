# #부분집합
# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)
'''
123      147 
456  ->  258       
789      369 

'''
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(i+1, 3):
#         arr[i][j], arr[j][i] =  arr[j][i], arr[i][j]
# print(arr)
# bit연산 하면 개빨라~


'''
부분집합을 비트 연산자로 
'''
# 
'''
arr = [1,2,4]

N = len(arr)
for i in range(1<<N):
    for j in range(N):
        if i & (1<< j):
            print(arr[j], end = ', ')

    print()
print()

'''


