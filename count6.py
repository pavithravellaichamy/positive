x=input()
count=0
for i in range(0,len(x)):
    if(x[i].isdigit()!=True and x[i].isalpha()!=True and x[i]!=' '):
        count=count+1
print(count)
