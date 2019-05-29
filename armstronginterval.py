l,u=list(map(int,input().split()))  
for n in range(l,u):  
   sum=0  
   t=n 
   while t > 0:  
       d=t%10  
       sum+=d**3  
       t//=10  
       if n==sum:  
            print(n,end=' ')  
