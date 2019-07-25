y=input()
x=input()
n=[]
l=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,len(x)):
    if x[i] not in l:
        m=x[i]
        n.append(m)
    else:
        continue
print("".join(map(str,n[::-1])))
