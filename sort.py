n1=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(" ".join(map(str,a)))
