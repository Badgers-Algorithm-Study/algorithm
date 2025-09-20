import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = 0
for i in range(M):
    A = int(input())
    cnt += A

ans = cnt // N
ans2 = cnt % N
if ans2 != 0:
    ans += 1
    
print(ans) 