#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15903                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lwk9589 <boj.kr/u/lwk9589>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15903                          #+#        #+#      #+#     #
#    Solved: 2025/08/23 14:36:57 by lwk9589       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline
import heapq
n, m = map(int, input().split())
cards = list(map(int, input().split()))
deck = []

# 카드덱 만들기
for x in cards:
    heapq.heappush(deck, x)

# 만든 카드덱에서 카드 합체 m번 해버리기
for _ in range(m):
    a = heapq.heappop(deck)
    b = heapq.heappop(deck)
    heapq.heappush(deck, a+b)
    heapq.heappush(deck, a+b)

print(sum(deck))