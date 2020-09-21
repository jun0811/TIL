# 연습문제
'''첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 "부모 자식" 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가
자식을 의미한다. 간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면
자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.
- 13 (정점의 개수)
- 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])
        print(node, end = ' ')
        

V = int(input()) # 정점
E = V - 1   # 간선
tree = [[0] * 3 for _ in range(V + 1)]
temp = list(map(int, input().split()))
cnt = 0
# tree 저장
# for i in range(E):
#     p, c = temp[i*2], temp[i*2+1]
#     if tree[p][0] == 0: # 왼쪽부터 채우기
#         tree[p][0] = c
#     else:
#         tree[p][1] = c
#     tree[c][2] = p

# for t in tree:
#     print(*t)

preorder(1)
print(cnt)

for i in range(E):
    p,c = temp[i*2] , temp[i*2+1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p