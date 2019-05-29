n=int(input()) 
l=len(str(n))
sum=0
t=n
while(t!=0):
	sum=sum+((t%10)**l)
	t=t//10
if sum==n:
	print("yes")
else:
	print("no")
