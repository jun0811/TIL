# k번째 작은 것을 찾기
def select(a, k):
    for i in range(0,k): # k번 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min] , a[i]
    return a[k-1] #마지막꺼

arr = [ 13, 11, 12,11, 55, 1, 3]
print(select(arr,1))