import math
INF=math.inf
N,M=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]

# print(lst)

house=[]
chi=[]

for i in range(N):
    for j in range(N):
        if lst[i][j]==1:
            house.append([i,j])
        elif lst[i][j]==2:
            chi.append([i,j])

print(house)

mindist=[INF for _ in range(M)]

for r,c in house:
    for r2,c2 in chi:
        dist=abs(r2-r)+abs(c2-c)
        if dist < max(mindist):
            mindist.pop(max(mindist))
            mindist.append(dist)
            
print(mindist)