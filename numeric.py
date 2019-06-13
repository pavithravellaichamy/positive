x=input()
count=0
d=0
for i in range(0,len(x)): 
    if x[i].isalpha()==True:
        d=d+1        
    if(x[i].isdigit()==True or x[i]=='.'):
        count=count+1
if(count>0 and d==0):
    print("Yes")
else:
    print("No")
        
