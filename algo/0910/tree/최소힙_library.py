# 최소합만 지원

import heapq

heap1 = [7, 2, 5, 3, 4, 6]
print(heap1)
# 쉽게 최소힙으로 전환
heapq.heapify(heap1)
print(heap1)

# 1을 추가해서 힙으로 만들기
heapq.heappush(heap1, 1)
print(heap1)

while heap1:
    print(heapq.heappop(heap1), end=' ')
print()

###################################

# 최대힙은?
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i]))
heapq.heppush(heap2, (-1, 1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end=' ')
    # print(heapq.heappop(heap2)* -1, end = '') 형태도 가능
