def Pd(word, n):
    # 글자길이 M word길이 N
        for i in range(len(word)-M+1):
            if word[i:M+i] == word[i:M+i][::-1]:
                result.append(word[i:i+M])



T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    result = []
    for word in words:
        Pd(word,M)
    sero_list = []
    sero = ''
    for y in range(N):
        for word in words:
            sero += word[y]
        sero_list.append(sero)
        sero = ''
    for word in sero_list:
        Pd(word,M)
    # print(result)
            
    print("#{} {}".format(tc, ''.join(result)))



