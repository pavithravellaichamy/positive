import math
x=int(input())
if(x<60):
    print("0 "+str(x))
elif(x==60):
    print("1 0")
elif (x>60):
    y=x/60
    z=math.floor(y)
    print(z,end=' ')
    m=z*60
    print(x-m)
 
