xy=input()
count=0
for i in range(0,len(xy)):
    if(xy[i].isdigit()==True):
        count=count+1
print(count)
