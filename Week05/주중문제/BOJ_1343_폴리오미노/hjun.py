import sys
input = sys.stdin.readline
boardMap = input().rstrip()
boardMap = boardMap.replace("XXXX", "AAAA")
boardMap = boardMap.replace("XX", "BB")

if "X" in boardMap:
    print(-1)
else:
    print(boardMap)

# import sys
# input = sys.stdin.readline

# boardMap = list(input().strip())
# cnt = 0
# answer = []

# for i in range(len(boardMap)):
#     if boardMap[i] == 'X':
#         cnt += 1
#     else:
#         if cnt % 2 == 1:
#             answer = [-1]
#             cnt = 0
#             break
#         else:
#             temp = cnt // 4
#             temp2 = cnt % 4
#             for _ in range(temp):
#                 answer.append('A')
#                 answer.append('A')
#                 answer.append('A')
#                 answer.append('A')
#             for _ in range(temp2 - 1):
#                 answer.append('B')
#                 answer.append('B')
#             answer.append('.')
#             cnt = 0
# if cnt != 0:
#     if cnt % 2 == 1:
#             answer = [-1]
#             cnt = 0
#     else:
#         temp = cnt // 4
#         temp2 = cnt % 4
#         for _ in range(temp):
#             answer.append('A')
#             answer.append('A')
#             answer.append('A')
#             answer.append('A')
#         for _ in range(temp2 - 1):
#             answer.append('B')
#             answer.append('B')
#         cnt = 0
# for j in range(len(answer)):
#     print(answer[j], end="")   
            