# import sys
# sys.stdin = open('이진_input.txt')

'''
완전 이진 트리 이므로 부모 노드 따라 저장 안해도 된다.
루트 노드를 만나면 cnt 출력
'''
def traverse(node):
    global cnt
    global half
    global root
    if node:
        traverse(tree[node][0])
        traverse(tree[node][1])
        cnt+=1
        print(node) 
        if node == 1:
            root = cnt
        elif node == N//2: 
            half = cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0]*2 for _ in range(N+1)]
    for i in range(1,N+1):
        if 2 * i <= N:
            tree[i][0] = 2*i
        if 2 * i + 1 <= N:
            tree[i][1] = 2*i+1
    # print(tree)
    cnt = 0
    root = 0
    half = 0
    traverse(1)
    
    print('#{} {} {}'.format(tc, root, half))