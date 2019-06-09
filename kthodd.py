x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=x[0]
b=x[1]
c=[]
for i in range(0,len(y)):
    if(y[i]%2!=0):
        c.append(y[i])
for i in range(0,len(c)):
    if i==(b-1):
        print(c[i])
