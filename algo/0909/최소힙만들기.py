def heappush(value):
    global heapcount

    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur //2

    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        paren = cur// 2

def heappop():
    global heapcount
    retValue = heap[1]

    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1

    parent = 1
    child = parent * 2

    #좌측과 우측 중 작은 것의 위치를 child로
    if child+1 <= heapcount:    #우측 자식 존재
        if heap[child] > heap[child+1]:
            child = child + 1

    #자식노드가 존재하고 부모노드 > 자식노드
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 우측 자식 존재
            if heap[child] > heap[child + 1]:
                child = child + 1

    return retValue


heapcount = 0
temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heap = [0] * (N+1)
for i in range(N):
    heappush(temp[i])
    print(heap)

for i in range(N):
    print(heappop(), end = ' ')
print()
