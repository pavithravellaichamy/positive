x=list(map(int,input().split()))
y=x[0]
z=x[1]
a=abs(y-z)
if(a%2==0):
    print("even")
else:
    print("odd")
