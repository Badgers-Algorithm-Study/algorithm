# 19638번 센티와 마법의 뿅망치
# import sys
# input = sys.stdin.readline

# N, H, T = map(int, input().split())
# giants = []

# for i in range(N):
#     giants.append(int(input()))
       
# cnt = 0

# for i in range(T):
#     giants.sort()
    
#     # 제일 뒤에가 작은지 체크
#     if giants[-1] < H:
#         break
    
#     giants[-1] = giants[-1] / 2
#     cnt += 1

# giants.sort()

# if giants[-1] >= H:
#     print("No")
#     print(int(giants[-1]))
# else:
#     print("Yes")
#     print(cnt)
    
    
import heapq
import sys
input = sys.stdin.readline

N, H, T = map(int, input().split())
giants = []

for i in range(N):
    height = int(input())
    heapq.heappush(giants, -height)
    
cnt = 0

for i in range(T):
    
    check = heapq.heappop(giants)
    check = -check
    
    if check < H:
        heapq.heappush(giants, -check)
        break
    
    if check == 1:
        heapq.heappush(giants, -check)
        continue
    
    check = check / 2
    cnt += 1
    heapq.heappush(giants, -check)

check = heapq.heappop(giants)
check = -check

if  check >= H:
    print("NO")
    print(int(check))
else:
    print("YES")
    print(cnt)

