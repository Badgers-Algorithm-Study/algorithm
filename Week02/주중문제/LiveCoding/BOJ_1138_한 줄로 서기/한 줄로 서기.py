import sys
input = sys.stdin.readline


N = int(input())
my_left = list(map(int, input().split()))

result = [0] * N # 빈 자리 만들기

for i in range(N): # 0부터 N-1까지의 사람에 대해
    count = 0
    for j in range(N): # 0부터 N-1까지의 자리 배치
        if result[j] == 0: # 아직 자리가 비어있다면
            if count == my_left[i]: # 왼쪽에 있어야 할 사람 수와 같다면
                result[j] = i + 1 # 사람 번호는 i+1
                break # 자리 배치 완료, 다음 사람으로
            count += 1 # 빈 자리 수 증가
print(*result)