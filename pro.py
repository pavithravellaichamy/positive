x=list(map(str,input().split()))
a=int(x[0])
b=x[1]
c=int(x[2])
if(b=='%'):
    print(a%c)
else:
    print(a//c)
