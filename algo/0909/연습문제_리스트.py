def pr(root):
    print(root, end=' ')
    if len(E[root])>0:
        pr(E[root][0])
    if len(E[root])>1:
        pr(E[root][1])

#    for child in E[root]:
#        pr(child)

V = int(input())
S = list(map(int, input().split()))

E = {k:[] for k in range(1, V + 1)}

i = 0
while i < len(S):
    E[S[i]].append(S[i+1])
    i += 2
print(E)

i= S[0]
pr(i)
