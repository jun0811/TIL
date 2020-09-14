def inorder(node): 
    global cnt
    if node == 0:
        return
    # 전위
    cnt += 1
    inorder(left[node])
    # 중위
    inorder(right[node])
    # 후위
 
for test_case in range(1, int(input()) + 1):
    E,N = map(int, input().split())
    arr = list(map(int, input().split()))
    # 구현1
    left = [0]*(E+2) # 첫번째 자식
    right = [0]*(E+2) # 두번째 자식
    # 구현2
    for i in range(0,len(arr),2): 
        papa, baby = arr[i], arr[i+1] # 부모 - 자식
        if left[papa]: # 0이 아니고 첫번째에 값이 있으면
            right[papa]=baby # 두번째에 보관
        else: # 0이면
            left[papa]=baby # 첫번째에 보관
 
    cnt = 0
    inorder(N)
    print('#{} {}'.format(test_case,cnt))