x1=int(input())
a=1
b=1
for i in range(0,x1):
    if i<=1:
        temp=1
    else:
        temp=a+b
        a=b
        b=temp
    print(temp,end=' ')
