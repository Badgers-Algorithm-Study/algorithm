import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

com = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    com[b].append(a)

check = [0 for _ in range(N+1)]


def dfs(n, v) : 
    cnt = 1
    v[n] = 1
      
    for y in com[n] :
        if v[y] == 0 :
            cnt += dfs(y,v)
    return cnt

mx = 0
ans = []
for i in range(1,N+1) : 
    visit = [0 for _ in range(N+1)]
    check[i] = dfs(i, visit)
    if mx < check[i] :
        ans = [i]
        mx = check[i]
    elif mx == check[i] :
        ans.append(i)


print(*ans)