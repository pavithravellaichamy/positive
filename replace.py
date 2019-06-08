xy=input()
n=len(xy)
if n%2!=0:
     print(xy[:n//2]+"*"+xy[n//2+1:])
else:
     print(xy[:n//2-1]+"**"+xy[n//2+1:])
