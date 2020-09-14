#horspoll algorithm(보이어무어의 단순버전)
skip = [M]*128 #a~z, A~Z
i = 0
j = M-1
for i in range(M-1):
    skip[ord(p[i])] = M-1-i

i = 0
while i < N-M:
    while j >= 0:
        if p[j] != t[i+j]:
            i += skip[ord(t[i+j])]
            break
        j -= 1
    if j==-1:
        return i
return -1