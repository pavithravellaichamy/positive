x=input()
d=0
count=0
for i in range(0,len(x)):
    if(x[i].isalpha()==True):
        count=count+1
    if(x[i].isdigit()==True):
        d=d+1
if(count>0 and d>0):
    print("Yes")
else:
    print("No")
