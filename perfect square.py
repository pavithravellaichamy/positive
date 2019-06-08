import math
n=list(map(int,input().split()))
a=n[0]
b=n[1]
n1=a*b
root = math.sqrt(n1)
if int(root+0.5)**2==n1:
    print("yes")
else:
    print("no")
