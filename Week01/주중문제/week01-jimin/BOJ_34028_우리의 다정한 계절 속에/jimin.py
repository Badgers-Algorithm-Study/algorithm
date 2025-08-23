A,B,C= map(int, input().split())

SA=2015
SB=3
SC=1
cnt=0
while A>=SA:
    if A>SA:
        cnt+=4
        SA+=1
    else:
        if SA==A:
            if SB<=B:
                if SB<=5 and SB>=3:
                    cnt+=1
                    SB=6
                    SC=1
                    
                elif SB<=8:
                    cnt+=1
                    SB=9
                    SC=1
                    
                elif SB<=11:
                    cnt+=1
                    SB=12
                    SC=1
                    
                else:
                    if SB==12:
                        cnt+=1
                        SA+=1
                        SB=3
                        SC=1
            else:
                break             
        else:
            break

print(cnt+1)