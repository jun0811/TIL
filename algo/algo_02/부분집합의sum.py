# A : 1~12
# 원소의 합이 k인 부분집합의 갯수 /// 없으면 0 출력

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int, input().split())

    A = [1,2,3,4,5,6,7,8,9,10,11,12] 

    cnt = 0
    for i in range(1<<len(A)):
        temp = [ ]
        for j in range(len(A)):
            if i& 1<<j:
                temp.append(A[j])
        
        if len(temp) == N:
            if sum(temp) == K:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))