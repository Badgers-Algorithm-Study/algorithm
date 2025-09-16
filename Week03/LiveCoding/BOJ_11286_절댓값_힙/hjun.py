import sys
import heapq
input = sys.stdin.readline

N = int(input())

absoluteArr = []

for i in range(N):
    x = int(input())
    
    if (x != 0) : # 0 이 아니라면
        heapq.heappush(absoluteArr, x)      
        
    else: #0 이면
        if(len(absoluteArr) == 0): 
            print(0)
        else:
            # 절댓값이 가장 작은 값 출력 후 제거
            # 여러개인 경우 제일 작은거 출력 후 제거
            beforeMin = float("inf")
            ans = 0
            temp =[]
            while len(absoluteArr) != 0:
                next = heapq.heappop(absoluteArr)
                if beforeMin > abs(next):
                    beforeMin = abs(next)
                    ans = next
                    temp.append(next)
                else:
                    break                
                
            print(ans)
            temp.pop()
            for k in temp:
                heapq.heappush(absoluteArr, k)