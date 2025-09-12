import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
cnt = 1

dic = {i : [] for i in range(1, N + 1)}
cntL = [1 for _ in range(N)]

def dfs(n):
    global cnt, visit
    visit[n] = 1
    if cntL[n-1] != 1:
        cnt += cntL[n-1]
        return
    for k in dic[n]:
        
        if visit[k] == 0:
            cnt += 1
            dfs(k)
    

for i in range(M):
    A, B = map(int, input().split())
    dic[B].append(A)
    
for i in range(1, N+1):
    visit = [0 for _ in range(N+1)]
    cnt = 1
    dfs(i)
    cntL[i-1] = cnt
    
maxV = max(cntL)

for j in range(N):
    if maxV == cntL[j]:
        print(j+1)



  
