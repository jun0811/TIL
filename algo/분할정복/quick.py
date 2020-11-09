# quick


def quickSort(l, r):
    if l<r:
        pivot = partition(l,r)
        quickSort(l,pivot-1)
        quickSort(pivot+1,r)

def partition(l,r):
    p = r
    i = l-1
    for j in range(l,r):
        if a[j] <= a[p]:
            i+=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[p] = a[p], a[i+1]
    return i+1

a = [4 ,3, 5, 6, 2, 4, 1]

quickSort(0,len(a)-1)

print(a)