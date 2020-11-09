def merge(left,right):
    global cnt
    idxl = idxr = 0
    res = []
    # print(left)
    # print(right)
    if left[-1] > right[-1]:
        cnt +=1
    while idxl<len(left) and idxr < len(right):
        if left[idxl] <right[idxr]:
            res.append(left[idxl])
            idxl += 1
        else:
            res.append(right[idxr])
            idxr += 1

    if idxl< len(left):
        while idxl < len(left):
            res.append(left[idxl])
            idxl += 1
    if idxr< len(right):
        while idxr < len(right):
            res.append(right[idxr])
            idxr += 1
    return res

def mergeSort(a):
    if len(a) == 1:
        return a
    else:
        m = len(a)//2
        left = mergeSort(a[:m])
        right = mergeSort(a[m:])
        # res = merge(left,right)
    return merge(left,right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    result = mergeSort(a)
    print('#{} {} {}'.format(tc, result[N//2], cnt))