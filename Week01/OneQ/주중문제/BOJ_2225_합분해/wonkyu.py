#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2225                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lwk9589 <boj.kr/u/lwk9589>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2225                           #+#        #+#      #+#     #
#    Solved: 2025/08/20 21:31:12 by lwk9589       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0]*(N+1) for _ in range(K+1)]

# 베이스 케이스 
for n in range(N+1):
    dp[1][n] = 1
for k in range(1, K+1):
    dp[k][0] = 1

# 점화식
for k in range(2, K+1):
    for n in range(1, N+1):
        dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1000000000

print(dp[K][N])