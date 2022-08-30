# 1. 전화번호를 인자로 받아, 각 숫자 중 홀수만 더해서 합계를 리턴하는 함수
def sum_odd(phone_number):
    sum_value = 0
    # 전화번호에서 하나씩 꺼내자
    for number in phone_number:
        # print(number)
        # 문자 -> 숫자
        number = int(number)
        # 홀수인지 구분
        if number % 2 != 0:
            # print(number)
            # 합계 구하자
            sum_value += number
    return sum_value

result = sum_odd('01012345678')
print(result)

