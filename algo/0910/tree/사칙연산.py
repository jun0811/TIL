import sys
sys.stdin = open("사칙연산_input.txt", "r")

# 사칙연산

# 아이디어
# 3열 행렬로 데이터를 받는다.(키값, 좌, 우)
# 후위 순회를 사용
# 후위 순회를 거쳐서 연산을 한뒤 다시 재귀함수에 넣는다.

 

for t in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        tree[i] = list(map(str, input().split()))
 
    for j in range(N, 0, -1):
        if tree[j][1].isdigit():
            for k in range(1, N+1):
                if tree[j][0] in tree[k][2:]:
                    tree[k][tree[k].index(tree[j][0])] = int(tree[j][1])
                    break

        else:
            if tree[j][1] == '+':
                tree[j][1] = int(tree[j][2]) + int(tree[j][3])
            elif tree[j][1] == '-':
                tree[j][1] = int(tree[j][2]) - int(tree[j][3])
            elif tree[j][1] == '*':
                tree[j][1] = int(tree[j][2]) * int(tree[j][3])
            elif tree[j][1] == '/':
                tree[j][1] = int(tree[j][2]) / int(tree[j][3])
            for k in range(1, N+1):
                if tree[j][0] in tree[k][2:]:
                    tree[k][tree[k].index(tree[j][0])] = tree[j][1]
                    break
                       
    print('#{} {}'.format(t, int(tree[1][1])))



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
