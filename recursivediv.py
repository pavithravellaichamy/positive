x=int(input())
while x%2==0:
    x=x/2
    if x%2!=0:
        break
print(int(x))
