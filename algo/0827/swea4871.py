# stack
# def dfs(n):
#     visited[n] = True
#     for i in link[n]:
#         if not visited[i]:
#             dfs(i)
            


# T = int(input())
# for tc in range(1,T+1):
#     V, E = map(int, input().split())
#     info = [list(map(int, input().split())) for _ in range(E)]
#     S, G = map(int, input().split())
#     visited = [False] * 50
#     link = [[] for _ in range(V+1)]
#     for i in range(E):
#         link[info[i][0]].append(info[i][1]) 
#     # print(link)
#     dfs(S)
#     if visited[G]:
#         print('#{} 1'.format(tc))
#     else:
#         print('#{} 0'.format(tc))
    
# def dfs(n):
#     visited[n] = True
#     for i in link[n]:
#         if not visited[i]:
#             dfs(i)


# T = int(input())
# for tc in range(1,T+1):
#     V, E = map(int, input().split())
#     info = [list(map(int, input().split())) for _ in range(E)]
#     S, G = map(int, input().split())
#     visited = [False] * 50 
#     link = [[] for _ in range(V+1)]
#     for i in range(E):
#         link[info[i][0]].append(info[i][1])

#     dfs(S)
#     if visited[G]:
#         print('#{} 1'.format(tc))
#     else:
#         print('#{} 0'.format(tc))

# DFS
# DFS
# DFS

def DFS(n):
    visited[n] = True
    for i in link[n]:
        if not visited[i]:
            DFS(i)


T = int(input())
for test_case in range(1,T+1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)] 
    S, G = map(int, input().split()) 
    visited = [False]*51
    link = [[] for i in range(V+1)] 
    for i in range(E):
        link[line[i][0]].append(line[i][1])

    DFS(S)
    if visited[G]:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))