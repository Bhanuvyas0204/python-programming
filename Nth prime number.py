x=int(input())
n,c=1,0
while(c<x):
    n+=1
    for i in range(2,n+1):
        if(n%i==0):
            break
    if(i==n):
        c=c+1
print(n)
