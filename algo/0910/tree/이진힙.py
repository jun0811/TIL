import sys
sys.stdin = open("이진힙_input.txt", "r")

# 이진 힙

# 아이디어 
# 최소힙 생성 알고리즘
# 마지막 노드 확인
# 마지막 노드에서 조상을 타고 올라가는 알고리즘 생성
# 누적합 구하기

def push(value):
    global hpcnt
    hpcnt += 1
    heap[hpcnt] = value
    # 순서를 바꿔준다.
    cur = hpcnt
    parent = cur // 2

    # 루트가 아니면서 부모값이 자식값보다 클때 바꿔준다.(최대힙은 반대)
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        # 변수 초기화를 통해 while문 반복될 수 있도록 한다.
        cur = parent
        parent = cur // 2

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * (N+1)
    hpcnt = 0
    for i in nums:
        push(i)
    
    total = 0
    while N != 1:
        N = N // 2
        total += heap[N]
        
    print('#{} {}'.format(t, total))







