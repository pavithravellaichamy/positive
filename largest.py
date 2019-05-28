a=list(map(int,input().split()))
b=a[0]
c=a[1]
d=a[2]
if b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)
