# 1. 휴대전화번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력하자
phone_number = '010-4658-7240'
# for i in phone_number:
#     if i=='-' or i==' 'or i=='/':
#         continue
#     print(i, end='')
# print()
phone_number = phone_number.replace('-', '')
phone_number = phone_number.replace('/', '')
phone_number = phone_number.replace(' ', '')
print(phone_number)
#>>01046587240
print('-'*30)

# 2. 학년->학년, 반, 학과, 번호 출력하기
# student_number = 2108
# grade = student_number/1000
# cl = student_number/(1000*grade)
#
# if(cl=='1' or cl=='2'):

# print(grade)

#>> 2학년 1반 뉴미디어 소프트웨어과 08번
#>> 2학년 1반 뉴미디어 소프트웨어과 8번
print('-'*30)

# 3. 369게임
# for i in range(1, 101):
#     if(i < 10):
#         if(i % 3 == 0):
#             print('짝')
#         else:
#             print(i)
#     elif(i%10==3 or i%10==6 or i%10==9):
#         print('짝')
#     elif(i/10==3 or i/10==6 or i/10==9):
#         print('짝')
#     else:
#         print(i)

#>> 1 2 짝 4 5 짝 ... 짝짝 100

