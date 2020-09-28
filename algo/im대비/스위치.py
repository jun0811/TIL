import sys
sys.stdin = open('스위치.txt')
def man(v):
    for i in range(v-1, N, v):
        if status[i] == 1:
            status[i] = 0
        else:
            status[i] = 1 

def woman(v):
    l = v
    r = v
    while (status[l-1] == status[r+1]) and l >=0 and r<N:
        l -= 1 
        r += 1
    # print(l,r)
    for i in range(l+1,r):
        if status[i]:
            status[i] = 0
        else:
            status[i] = 1

N = int(input())
status = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    s, n = map(int,input().split())
    if s == 1:
        man(n)
        # print(status)
    else:
        woman(n-1)
        # print(status)

for i in status:
    print(i, end= " ")