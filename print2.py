n1=list(map(str,input().split()))
a=n1[0]
b=int(n1[1])
for i in range(0,len(a)):
    if(i<b):
        print(a[i],end='')
