import sys
import heapq
N = int(sys.stdin.readline())

meet = []
for _ in range(N) :
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(meet, [e, s])

end, start = heapq.heappop(meet)
cnt = 1
while meet :
    e, s = heapq.heappop(meet)
    if end <= s :
        cnt += 1
        end = e

print(cnt)

