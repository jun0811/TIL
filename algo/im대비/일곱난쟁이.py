
dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

for i in range(1<<len(dwarf)):
    temp = []
    for j in range(len(dwarf)):
        if i & 1<<j:
            temp.append(dwarf[j])
    # print(temp)
    if len(temp) == 7 and sum(temp) == 100:
        break

temp.sort()
for t in temp:
    print(t)