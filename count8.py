x=list(map(str,input().split()))
y=list(map(str,input().split()))
count=0
a=x[1]
for i in range(0,len(y)):
    if(a==y[i]):
        count=count+1
print(count)
