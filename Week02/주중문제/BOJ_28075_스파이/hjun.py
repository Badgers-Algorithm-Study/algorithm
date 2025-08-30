import sys
input = sys.stdin.readline

N, M = map(int, input().split())

get_list_s = list(input().split())

see_list_s = list(input().split())

get_list =[]
see_list =[]

for i in range(3):
    get_list.append(int(get_list_s[i]))
    see_list.append(int(see_list_s[i]))

# 한곳에서 미션 수행시 절반으로 떨어짐
# n일 m이상의 진척도
# 수행가능한 방법

cnt = 0

def mission(n, i, m, s):
    global cnt
    
    get_temp_list = [0 , 0, 0]
    see_temp_list = [0 , 0, 0]
    
    print(n,i,m,s)
    if n == 1:
        if s >= M:
            cnt += 1
        return 0
            
    for i in range(3):
        get_temp_list[i] = get_list[i]
        see_temp_list[i] = see_list[i]

    get_temp_list[i] = int(get_list[i] / 2)
    see_temp_list[i] = int(see_list[i] / 2)

    mission(n-1, 0, 0, s+get_temp_list[0])
    mission(n-1, 1, 0, s+get_temp_list[1])
    mission(n-1, 2, 0, s+get_temp_list[2])
    mission(n-1, 0, 1, s+see_temp_list[0])
    mission(n-1, 1, 1, s+see_temp_list[1])
    mission(n-1, 2, 1, s+see_temp_list[2])


mission(N, 0, 0, get_list[0])
mission(N, 1, 0, get_list[1])
mission(N, 2, 0, get_list[2])
mission(N, 0, 1, see_list[0])
mission(N, 1, 1, see_list[1])
mission(N, 2, 1, see_list[2])

print(cnt)