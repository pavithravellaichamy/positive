x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=x[0]
b=x[1]
for i in range(0,len(y)):
    for j in range(i+1,len(y)):
        if(y[i]>y[j]):
            y[i],y[i+1]=y[i+1],y[i]
for i in range(0,len(y)):
    if i==(b-1):
        print(y[i])
