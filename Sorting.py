a = [0,5,3,10,22,11,6,12,4,3]
l = len(a)
sort1 = False
while(not sort1):
    sort1 = True

    for i in range(l -1):
        if (a[i] > a[i+1]):
            a[i],a[i+1] = a[i+1],a[i]
            sort1 = False
print(a)