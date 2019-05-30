y=int(input())
x=list(map(int,input().split()))
sum=0
y=len(x)
for i in range(0,y):
  sum=sum+x[i]
print(int(sum/y))
