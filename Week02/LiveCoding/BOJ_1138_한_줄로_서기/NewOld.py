import sys
import heapq
from collections import deque

N = int(sys.stdin.readline())

mem = list(map(int, sys.stdin.readline().split()))

spot = [0 for _ in range(N)]

for i in range(N) :
    if mem[i] == 0 :
        for j in range(N) :
            if spot[j] == 0 :
                spot[j] = i+1
                break
    else :
        cnt = mem[i]
        for j in range(N) :
            if spot[j] == 0 :
                if cnt > 0 :
                    cnt -= 1
                else :
                    spot[j] = i+1
                    break
print(*spot)



# seat = []

# for i in range(N) :
#     heapq.heappush(seat, [mem[i], i+1])

# line = []

# zero = deque()
# front, idx = heapq.heappop(seat) 
# cnt = 1
# line.append(idx)

# while seat :
#     front, idx = heapq.heappop(seat) 
#     if front == 0 :
#         zero.append(idx)
#     else :
#         if cnt == front :
#             line.append(idx)
#         elif cnt < front :
#             if zero :
#                 i = zero.popleft()
#                 line.append(i)
#             line.append(idx)
#             cnt = front

# while zero :
#     i = zero.popleft()
#     line.append(i)
    
# print(*line)


