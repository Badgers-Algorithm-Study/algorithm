import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
lst=[]
for _ in range(M):
    lst.append(list(input()))

print(lst)

visited=[[False]*N for _ in range(M)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

w=0
b=0

def bfs(x,y,t):
    q=deque([x,y])
    visited[x][y]=True
    cnt=1
    while q:
        cx,cy=q.popleft()
        
        for i in range(4):
            nx,ny=cx+dx[i],cy+dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and lst[nx][ny]==t:
                visited[nx][ny]==True
                q.append((nx,ny))
                cnt+=1
    return cnt

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            t=lst[i][j]
            ns=bfs(i,j,t)
            if t=="W":
                w+=