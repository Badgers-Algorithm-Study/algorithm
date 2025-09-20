import sys
input = sys.stdin.readline

N, M = map(int ,input().split())
mapInfo = []
chicken = []
house = []
chickenLen = []
ar = []

for i in range(N):
    mapInfo.append(list(input().split()))  
    
for i in range(N):
    for j in range(N):
        if mapInfo[i][j] == '2':
            chicken.append([i,j])
        elif mapInfo[i][j] == '1':
            house.append([i, j])
            

if len(chicken) == M:
    for check in house:
        temp = []
        houseX, houseY = check
        for chick in chicken:
            chickX, chickY = chick
            temp.append(abs(houseX - chickX) + abs(houseY - chickY))
        ar.append(temp)
        chickenLen.append(min(temp))  
    print(sum(chickenLen))

# 치킨 집 개수 줄여야 할 때
# else :
#     for check in house:
#         temp = []
#         houseX, houseY = check
#         for chick in chicken:
#             chickX, chickY = chick
#             temp.append(abs(houseX - chickX) + abs(houseY - chickY))
#         ar.append(temp)
#         chickenLen.append(min(temp))

    
