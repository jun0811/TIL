import sys
sys.stdin = open("노드의합_input.txt", "r")

# 노드의 합

# 아이디어
# 완전이진트리 - 1차원배열 사용가능
# 재귀함수(후위순회?)
# node에 수가 저장되어있으면 수를 반환
# 수가 없으면 합으로 재귀호출

def upsum(node):
    if node:
        upsum(tree[node][0])
        upsum(tree[node][1])
        if tree[node][2]:
            tree[node//2][2] += tree[node][2]

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    # 완전 이진 트리 생성
    tree = [[0] * 3 for _ in range(N+1)]
    for i in range(1, N+1):
        if 2 * i <= N:
            tree[i][0] = 2 * i
        if 2 * i + 1 <= N:
            tree[i][1] = 2 * i + 1   
    # 리프노드 값 입력
    for j in range(M):
        no, value = map(int, input().split())
        tree[no][2] = value
    s = []
    upsum(1)
    print('#{} {}'.format(t, tree[L][2]))