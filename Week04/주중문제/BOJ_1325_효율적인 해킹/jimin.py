import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[b].append(a)

def bfs(s):
    q=deque()
    q.append(s)
    visited = [False] * (N + 1)
    visited[s]=True
    cnt=1
    while q:
        v=q.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w]=True
                cnt+=1
                q.append(w)
    return cnt

result=[]
for i in range(1,N+1):
    result.append(bfs(i))
max_cnt=max(result)

for i in range(N):
    if result[i]==max_cnt:
        print(i+1,end=" ")