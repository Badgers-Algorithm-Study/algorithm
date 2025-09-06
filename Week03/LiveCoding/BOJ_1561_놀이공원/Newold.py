import sys, heapq

N, M = map(int, sys.stdin.readline().split())

time = list(map(int, sys.stdin.readline().split()))
check = [0 for _ in range(M)]


q = []
ans = 0
for  _ in range(N) :
    if 0 in check :
        i = check.index(0)
        check[i] += 1
        heapq.heappush(q, [time[i] * check[i], i])
        ans = i

    else :
        t, idx = heapq.heappop(q)
        check[idx] += 1
        heapq.heappush(q, [time[idx] * check[idx], idx])
        ans = idx

print(ans+1)