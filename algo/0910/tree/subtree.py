import sys
sys.stdin = open("subtree_input.txt", "r")

# 서브트리

# 아이디어
# 후위순회
# 노드를 만날때 까지 카운트
# 노드를 만나면 리턴

def find(node):
    global cnt
    if node:
        cnt += 1
        find(tree[node][0])
        find(tree[node][1])


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    # 이진트리 
    tree = [[0] * 2 for _ in range(E+2)]
    # 단방향(자식노드만 기록)
    info = list(map(int, input().split()))
    for i in range(E):
        p, s = info[i*2], info[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = s
        else:
            tree[p][1] = s
    cnt = 0

    find(N)
    print('#{} {}'.format(t,cnt))

