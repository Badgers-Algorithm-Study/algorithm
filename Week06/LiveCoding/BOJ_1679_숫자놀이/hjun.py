import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
K = int(input())
check = 2
dp = [0, 1]

while True:
    dp.append(10000000)
    
    for i in range(len(numList)):
        if check-numList[i] >= 0:
            dp[check] = min(dp[check], dp[check-numList[i]] + 1) 
               
    if dp[check] == 10000000:
        break
    
    if dp[check] > K*N:
        break
    
    print(check)
    print(dp)
    print()
    
    check += 1

print(check)


    
    

   
    
    
    
    
    
