# dfs
# start위치 , 방문 여부 확인 필요
# 다른 언어는 이중리스트에서 크기가 다른걸 만들기가 어려워서 
# [인접여부 리스트를 0도 너어주어야한다]
# 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7

def dfs(v):
    visited[v] = 1
    print(v, end= ' ')
    for s in line[v]:
        if not visited[s]:
            visited[s] = 1
            dfs(s)
            
    


arr = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
line = [[] for i in range(max(arr)+1)]
# print(line)
visited = [0] * (max(arr) + 1)
for i in range(0,len(arr),2):
    line[arr[i]].append(arr[i+1])
    line[arr[i+1]].append(arr[i])

print(line)
dfs(1)