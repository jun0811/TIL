# swea4866
for tc in range(3):
    arr = input()
    S = []
    for ch in arr:
        if not S or ch != S[-1]:
            S.append(ch)
        else:
            S.pop()
    
    print(len(S))