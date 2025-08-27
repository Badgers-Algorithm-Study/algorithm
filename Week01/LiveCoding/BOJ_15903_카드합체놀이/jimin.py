
n,m=map(int, input().split())
cards=list(map(int,input().split()))


lst=[]
score=0
for _ in range(m):

    cards.sort()
    x=cards[0]
    y=cards[1]
    add=x+y
    cards.remove(x)
    cards.remove(y)
    cards.append(add)
    cards.append(add)        

print(sum(cards))