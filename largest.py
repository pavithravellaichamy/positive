a1=list(map(int,input().split()))
b=a1[0]
c=a1[1]
d=a1[2]
if b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)
