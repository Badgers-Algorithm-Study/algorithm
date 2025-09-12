import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N=int(input())
    
    s=1
    e=N
    result=0
    while s<=e:
        m=(s+e)//2
        if m*(m+1)//2<=N:
            result=m
            s=s+1
        else: 
            e=m-1        
    print(result)