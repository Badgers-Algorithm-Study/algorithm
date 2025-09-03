import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# 회의 종료 시간 기준으로 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))
maximum = 0
# 이전 회의 종료 시간 기록
end_time = 0

# 회의 시작 시간이 이전 회의 종료 시간보다 크거나 같으면
# 회의 가능 개수 증가, 이전 회의 종료 시간 갱신
for start, end in meetings:
    if start >= end_time:
        maximum += 1
        end_time = end

print(maximum)


