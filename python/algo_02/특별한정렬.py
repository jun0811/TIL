def select_max(arr, k):
    for i in range(k):
        max_n = i
        for j in range(i+1, len(arr)):
            if arr[max_n] < arr[j]:
                max_n = j
        arr[i], arr[max_n] = arr[max_n], arr[i]
    return str(arr[k-1])

def select_min(arr, k):
    for i in range(k):
        min_n = i
        for j in range(i+1, len(arr)):
            if arr[min_n] > arr[j]:
                min_n = j
        arr[i], arr[min_n] = arr[min_n], arr[i]
    return str(arr[k-1])



T = int(input())

for test_case in range(1,T+1): 
    N = int(input())

    numbers = list(map(int,input().split()))

    result  = []
    for i in range(1,6):
        result.append(select_max(numbers,i))
        result.append(select_min(numbers,i))

    a= ' '.join(result)
    print('#{} {}'.format(test_case, a))
