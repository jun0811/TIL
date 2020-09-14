# 탐색 알고리즘

def find(p,t):
    i , j = 0, 0
    while i<len(p) and j<len(t):
        if p[i] != t[j]:
            j = j-i
            i = -1
        i +=1
        j +=1 
        if len(p) == i:
            return 1
    return 0 



T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    result = find(str1,str2)
    print('#{} {}'.format(tc, result))