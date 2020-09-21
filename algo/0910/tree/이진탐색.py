# import sys
# sys.stdin = open("이진탐색_input.txt", "r")

# 이진탐색

# 아이디어
# 중위순회로 카운트하기(LVR)
# 루트 노드만나면 cnt 출력

# 중위 순회
def traverse(node):
    global cnt
    global half
    global root
    if node:
        traverse(tree[node][0])

        traverse(tree[node][1])
        cnt += 1
        print(node)
        if node == 1:
            root = cnt
        elif node == N // 2:  # 부모노드 라는 건데
            half = cnt


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(N)
    # 완전 이진 트리 생성
    tree = [[0] * 2 for _ in range(N+1)]
    for i in range(1, N+1):
        if 2 * i <= N:
            tree[i][0] = 2 * i
        if 2 * i + 1 <= N:
            tree[i][1] = 2 * i + 1
    print(tree)
    cnt = 0
    root = 0
    half = 0
    traverse(1)
    print('#{} {} {}'.format(t, root, half))