'''
13 ← 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


#import sys
#sys.stdin = open("input.txt", "r")


def preorder_traverse(T):
    if T:
        print("%d" % T, end=' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])

def postorder_traverse(T):
    if T:
        postorder_traverse(tree[T][0])
        postorder_traverse(tree[T][1])
        print("%d" % T, end=' ')

def inorder_traverse(T):
    if T:
        inorder_traverse(tree[T][0])
        print("%d" % T, end=' ')
        inorder_traverse(tree[T][1])

n = int(input())
tree = [[0] * 2 for _ in range(n + 1)]

templ = list(map(int, input().split()))

for i in range(len(templ) // 2):
    parent, child = templ[i * 2], templ[i * 2 + 1]
    if not tree[parent][0] :
        tree[parent][0] = child
    else:
        tree[parent][1] = child

print("pre: ", end="")
preorder_traverse(1)
print()
print("post: ", end="")
postorder_traverse(1)
print()
print("in: ", end="")
inorder_traverse(1)
