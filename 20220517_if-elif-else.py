# money = int(input('금액을 입력해주세요 : '))
# if money >= 10000:
#     print("택시를 타세요")
# elif money >= 720:
#     print("버스를 타세요")
# else:
#     print("걸어가세요")

# 배수 판별 문제
# num = int(input('정수를 입력하세요 : '))
# if num % 4 == 0:
#     print("4의 배수")
# elif num % 3 == 0:
#     print("3의 배수")
# elif num % 2 == 0:
#     print("2의 배수")

# 나이대 판별 문제
# age = int(input('나이를 입력하세요 '))
# if 10 <= age < 20:
#     print("10대")
# elif 30 <= age < 40:
#     print("30대")
# else:
#     print("10대, 30대가 아님")
# print("--------------------")
# print(str(age//10*10) + "대")

# 논리연산자 문제
# x = int(input('정수를 입력하세요 '))
# if 10 < x and x % 2 == 0:
#     print("10 초과 짝수")

# 등급 출력 문제
# score = int(input('점수를 입력하세요 : '))
# if 90 <= score <= 100:
#     print("A등급")
# elif 80 <= score < 90: # 80 <= score
#     print("B등급")
# elif 70 <= score < 80: # 70 <= score
#     print("C등급")
# elif 60 <= score < 70: # 60 <= score
#     print("D등급")
# elif 0 <= score < 60:  # 0 <= score
#     print("F등급")

# MBTI
# my_mbti = input('MBTI를 입력하세요 : ')
# if my_mbti == "isfp" or my_mbti == "ISFP":  #my_mbti.upper()
#     print("네트워크 개발자형")
# elif my_mbti == "infp" or my_mbti == "INFP":
#     print("블록체인형")
# else:
#     print("아직 개발중 입니다")

# 중첩 제어문
# x = int(input('정수를 입력하세요 : '))
# if x < 10:
#     if x % 2 == 0:
#         print("10초과 짝수")
#     else:
#         print("10초과 홀수")
# else:
#     print("10이하")

#
nicname = "JAYUN"
id = "python_ddabong"
password = "python"
ID = input('id를 입력하세요 : ')
pw = input('비밀번호를 입력하세요 : ')
if id == ID:
    if password == pw:
        print("환영합니다 "+nicname+"님")
    else:
        print("패스워드가 틀렸습니다")
else:
    print("알 수 없는 사용자입니다.")