T=int(input())

for _ in range(T):
    N=int(input())
    lst=list(map(str, input().split()))
    # print(lst)
    for i in range(4):
        print(lst[i][0])