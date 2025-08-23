#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 34028                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: lwk9589 <boj.kr/u/lwk9589>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/34028                          #+#        #+#      #+#     #
#    Solved: 2025/08/21 23:17:52 by lwk9589       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

# 데뷔일자
A, B, C = 2015, 1, 16

# 현재일자
D, E, F = map(int, input().split())

# 데뷔 일자의 계절 포함하기
count = 1 

# 데뷔 이후 맞이하는 첫 계졀
def first_season(y, m, d):
    for xm, yd in [[3, 1], [6, 1], [9, 1], [12, 1]]:
        if (m, d) < (xm, yd):
            return (y, xm, yd)
    return (y + 1, 3, 1) 

# 계절 단위로 카운트 단위 구분하기
def count_step(y, m, d):
    if m == 3:
        return (y, 6, 1)
    elif m == 6:
        return (y, 9, 1)
    elif m == 9:
        return (y, 12, 1)
    else:
        return (y + 1, 3, 1)
    
# 데뷔 이후 맞이하는 계절부터 카운트
y, m, d = first_season(A, B, C)
while (y, m, d) <= (D, E, F):
    y, m, d = count_step(y, m, d)
    count += 1

print(count)
