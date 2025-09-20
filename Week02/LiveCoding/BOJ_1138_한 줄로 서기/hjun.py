import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
left = list(map(int, input().split()))
answer = deque([])

for i in range(N):
    index = N - 1 - i
    temp = []
    if index == N:
        answer.append(N)
        continue
        
    leftNum = left[index]
    
    for j in range(i+1):
        if j == leftNum:
            temp.append(index+1)
            continue
        temp.append(answer.popleft())
        
    for j in temp:
        answer.append(j)
        
print(*answer)
        
        