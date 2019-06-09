x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=x[1]
sum=0
for i in range(0,len(y)):
    if i<a:
        sum=sum+y[i]
print(sum)
