T = int(input())
for tc in range(1,T+1):
    word = input() + '0'
    result = [word[0]]

    for i in range(1,len(word)):
        if len(result)==0: #같지 않으면 집어넣는다 
            result.append(word[i])
        elif (result[-1] != word[i]) :
            result.append(word[i])
        else: # 같은 놈이 나오면 pop을 한다  
            result.pop()
        if word[i+1] == '0':
            break
        # print(result)
    print('#{} {}'.format(tc, len(result))) # 

