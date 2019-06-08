x=int(input())
y=list(map(int,input().split()))
a=y[0]
b=y[1]
if a<x<b:
    print("yes")
else:
    print("no")
