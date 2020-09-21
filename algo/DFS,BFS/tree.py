'''
전위 순회
- 13 개의 노드
- 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(node):
    global cnt
    if node:
        preorder(tree[node][0])
        print(node, end = ' ') # 위치에 따른 순회 구조가 달라짐 
        preorder(tree[node][1])
        cnt += 1

V = int(input())
E = V-1
tree = [[0]*3  for _ in range(V+1)]
temp = list(map(int, input().split()))
cnt = 0
# [1 2 3 ] -> 1: 왼쪽 자식 ,2 : 오른쪽 자식 , 3: 부모 노드  
for i in range(E):
    p,c = temp[i*2], temp[i*2+1]
    if not tree[p][0]:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

preorder(1)
print('')
print(cnt)