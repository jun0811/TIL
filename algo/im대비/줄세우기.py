T = int(input())
arr = list(map(int, input().split()))
temp = []
for i in range(1,T+1):
    temp.insert(arr[i-1], i)
print(*list(reversed(temp)))