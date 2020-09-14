# def BubbleSort(a):
#     for i in range(len(a)-1, 0 , -1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a

# data = [ 53, 13,1234, 12,11 ,1]
# print(BubbleSort(data))

# 카운트 sort ->  시간 복잡도 n + k
# 가장 큰 정수를 알아야함
# '정수 자료만 가능'
def counting_sort(A, B, n):
    C = [0] * n
    # 카운팅 누적 소트
    #카운트
    for i in range(len(B)):
        C[A[i]] += 1
    #누적
    for i in range(1, len(C)):
        C[i] += C[i-1]

    #소트
    for k in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= -1
    print(C)


a = [5,3,1,2,3,4,0]
b = [0]*len(a)
c = counting_sort(a,b,10)
#print( c)