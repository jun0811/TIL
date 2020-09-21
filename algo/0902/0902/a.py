new_id ='...!@BaT#*..y.abcdefghijklm'
new_id.lower()
temp = []
for i in new_id:
    if i != '!' or i != '@' or i !=  '#' or i != '*':
        temp.append(i)
L = len(temp)
second = []
for i in range(1,L):
    if temp[i] == temp[i-1] == '.':
        temp.pop(i)
        temp.append('')

if temp[0] == '.': # 4단계
    temp.pop(0)

result = ''.join(temp)
print(result)
result.replace(' ','a')

result = result[:15]
for i in range(14):
    if result[-1] == '.':
        result = result[:-1]
    else:
        break
while len(result)< 3:
    result += result


answer = result
print(answer)