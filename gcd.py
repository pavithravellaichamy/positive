x=list(map(int,input().split()))
a=x[0]
b=x[1]
while b > 0:
    a, b = b, a % b
print(a)
