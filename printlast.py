x=list(map(str,input().split()))
a=x[0]
b=x[1]
d=[]
c=a[::-1]
for i in range(0,len(c)):
    if i<int(b):
      d.append(c[i])
e=d[::-1]
print("".join(map(str,e)))
