xy=int(input())
count1=0
for i in range(1,xy+1):
    if(xy%i==0):
        count1=count1+1
if count1<=2:
  print("yes")
else:
    print("no")
