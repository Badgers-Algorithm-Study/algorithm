import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수
for _ in range(T): # 각 테스트 케이스별로 시행
    N = int(input()) # 학생 수
    mbti = list(input().split()) # 각 학생별 MBTI
    if N > 32: # 학생 수가 32명을 초과하면 무조건 0
        print(0)
    else:
        min_dist = float('inf')
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    dist = 0
                    for l in range(4):
                        if mbti[i][l] != mbti[j][l]:
                            dist += 1
                        if mbti[i][l] != mbti[k][l]:
                            dist += 1
                        if mbti[j][l] != mbti[k][l]:
                            dist += 1
                    min_dist = min(min_dist, dist)
        print(min_dist)