# def preorder_traverse(T):
#     if T:
#         print('%d' %T, end=' ')
#         preorder_traverse(tree[T][0])
#         preorder_traverse(tree[T][1])

# def inorder_traverse(T):
#     if T:
#         inorder_traverse(tree[T][0])
#         print('%d' %T, end=' ')
#         inorder_traverse(tree[T][1])

# def postorder_traverse(T):
#     if T:
#         postorder_traverse(tree[T][0])
#         postorder_traverse(tree[T][1])
#         print('%d' %T, end=' ')

# for tc in range(1,11):
#     # 트리입력 
#     tree = [[0]*2 for _ in range(n+1)] #2차 
#     temp = list(map(int,input().split()))
#     for i in range(len(temp)//2):
#         p , c = temp[i*2], temp[i*2 +1]
#         if not tree[p][0]:
#             tree[p][0] = c
#         else:
#             tree[p][1] = c

# def t(i):
#     try: t(edges[int(i)][0])
#     except: pass
#     print(nodes[int(i)], end='')
#     try: t(edges[int(i)][1])
#     except: pass
 
# for tc in range(1, 11):
#     N = int(input())
#     nodes = [0]*(N+1)
#     edges = [[] for _ in range(N+1)]
#     info = [list(input().split()) for _ in range(N)]
#     for i in info:
#         nodes[int(i[0])] = i[1]
#         edges[int(i[0])].extend(i[2:])
#     print('#{}'.format(tc), end=' ')
#     t('1')
#     print()

def inorder(T):
    if T:
        inorder(tree[T][0])
        print('{}'.format(num_dict[str(T)]), end="")
        inorder(tree[T][1])
 
for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 2 for _ in range(N+1)]
 
    # 노드 숫자별 알파벳을 딕셔너리에 담기
    num_dict = {}
    for _ in range(N):
        li_tmp = list(input().split())
        num_dict[li_tmp[0]] = li_tmp[1]
        if len(li_tmp) == 4:
            tree[int(li_tmp[0])][0] = int(li_tmp[2])
            tree[int(li_tmp[0])][1] = int(li_tmp[3])
        elif len(li_tmp) == 3:
            tree[int(li_tmp[0])][0] = int(li_tmp[2])
 
    print('#{}'.format(tc), end=" ")
    inorder(1)
    print()