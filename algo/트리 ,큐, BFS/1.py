N,X = map(int,input().split())
a = list(map(int,input().split()))
small = []
for i in range(N) :
  if a[i] < X :
    small.append(a[i])

for s in small:
    print('{}'.format(s), end = " ")