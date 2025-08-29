import sys
input = sys.stdin.readline

Day, Rate = map(int, input().split())
IntelValue = list(map(int, input().split()))
SurveilValue = list(map(int, input().split()))

table = [IntelValue, SurveilValue] # 입력된 기여도 가치를 테이블로 만들기
target = max(IntelValue + SurveilValue) # 하루에 얻을 수 있는 최대 기여도는?

def calculate(duty, prev_place, total):
    if duty >= Day: # 모든 근무일이 끝나고
        if total >= Rate: # 목표 기여도를 달성 했으면
            return 1
        else:
            return 0
        
    remain = Day - duty # 남은 근무일 계산

    if total + remain * target < Rate: # 가지 쳐버리기
        return 0
    
    cases = 0 
    
    # 경우의 수 따져보기
    for task in range(2): # 임무 종류 2개
        for place in range(3): # 임무 지역 3곳
            gain = table[task][place]
            if place == prev_place: # 동일 지역 임무 시 기여도 반토막
                gain //= 2
            cases += calculate(duty + 1, place, min(Rate, total + gain))
    
    return cases

print(calculate(0, -1, 0))