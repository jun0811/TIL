# 조합 
arr = [1,2,3]
# temp = []
# for i in range(1<<len(a)):
#     for j in range(len(a)):
#         if i & 1<<j:
#             temp.append(a[j])
#     print(temp)
#     temp = []    
# 순열
def perm(n,k):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1)
            arr[k], arr[i] = arr[i], arr[k]

N = len(arr)
perm(N,0)
