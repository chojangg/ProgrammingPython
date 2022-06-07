# 1. 휴대전화번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력하자
phone_number = '010-4658-7240'
for i in phone_number:
    if i=='-' or i==' 'or i=='/':
        continue
    print(i, end='')
print()
phone_number = phone_number.replace('-', '')
phone_number = phone_number.replace('/', '')
phone_number = phone_number.replace(' ', '')
print(phone_number)
#>>01046587240
print('-'*30)

# 2. 학년->학년, 반, 학과, 번호 출력하기
student_number = '2108'
# if student_number[1] == '1' or student_number[1] == '2':
#     g = '뉴미디어소프트웨어과'
# elif student_number[1] == '3' or student_number[1] == '4':
#     g = '뉴미디어웹솔루션과'
# elif student_number[1] == '5' or student_number[1] == '6':
#     g = '뉴미디어디자인과'
majors = ['','뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과',
          '뉴미디어웹솔루션과', '뉴미디어디자인과','뉴미디어디자인과']
index = int(student_number[1])
g = majors[index-1]
print(f'{student_number[0]}학년 {student_number[1]}반')
print(f'{g} {int(student_number[2:])}번')

#>> 2학년 1반 뉴미디어 소프트웨어과 08번
#>> 2학년 1반 뉴미디어 소프트웨어과 8번
print('-'*30)

# 3. N-sum
number = 331
# n1 = (int)(number % 1000 / 100)
# n2 = (int)(number % 100 / 10)
# n3 = (int)(number % 10)
# print(n1+n2+n3)
#>>7
number = 523523
sum_val = 0
while True: # while number!=0
    if number == 0:
        break
    sum_val += number % 10
    sum_val += number // 10
print(sum_val)
# 숫자 한자리씩 빼서 계산하자
number_s = str(number)  # '523523'
sum_val2 = 0
for n in number_s:
    sum_val2 += int(n)
print(sum_val2)
# 나머지 = number % 10   #3
# number = number // 10   # 523523 -> 52352
# 나머지 = number % 10   #2
# number = number // 10   # 52352 -> 5235
# 나머지 = number % 10   #5
# number = number // 10   # 5235 -> 523
# 나머지 = number % 10   #3
# number = number // 10   # 523 -> 52
# 나머지 = number % 10   #2
# number = number // 10   # 52 -> 5
# 나머지 = number % 10   #5
# number = number // 10   # 5 -> 0
#>>20

# 4. 369게임
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

