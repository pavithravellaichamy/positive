y=int(input())
x=list(map(int,input().split()))
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]>x[j]):
            print(j-1)
            break
