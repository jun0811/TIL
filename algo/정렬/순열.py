arr = [1,2,3]

for i in arr:
    for j in arr:
        if i!=j:
            for k in arr:
                if k != i and k!=j:
                    print(i,j,k)