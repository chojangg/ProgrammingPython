# 사용한 시간(분)을 인자로 받아 pc방 요금을 리턴하는 fare_pc함수
'''
10분 당 1000원
1분 초과 해도 1000원 추가
'''

def fare_pc(minutes):
    # minutes을 10으로 나누자. 몫
    share = minutes // 10
    # 몫 * 1000 = 요금
    fare = share * 1000
    # minutes을 10으로 나눈 나머지가 있으면 +1000
    if minutes %10 !=0:
        fare += 1000
    return fare

print(fare_pc(3))
print(fare_pc(20))
print(fare_pc(34))
