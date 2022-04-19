greeting = 'hello'
to = 'world!'
say_hello = greeting + ', ' + to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to)
print("\"" + greeting + "\"")
print('\'' + greeting + '\'')
names = '''양다연
인소리
이예진
'''
print(names)

# *** indexing, slicing
names = '양다연인소리이예진'
print(names[2]) #'연'
print(names[4])  #'소'
print(names[8]) #'진'
print(names[-1])    #'진'
print(names[-2])    #'예'
print(names[-9])    #'양'
student_number = '2112'
print(student_number[0] + '학년')
print(f'{student_number[0]}학년')
print(f'{student_number[1]}반')
#'양다연인소리이예진'
print(names[2:5])   #[2]~[4]
print(names[2:4])   #연인
print(names[-7:-5])
print(names[4:7])   #소리이
print(names[7:9])   #예진
print(f'{student_number[2:4]}번')
print(f'{student_number[-2:]}번')    #start:end-1    [start:]: 끝까지
print(f'{student_number[0:2]}학년반')
print(f'{student_number[0:-2]}학년반')
print(f'{student_number[:-2]}학년반')  #start:end-1    [:end-1]: 앞까지
print(f'{student_number[:]}')  #start:end-1    [:]: 앞~끝까지

#문자열 함수
print(f'길이: {len(student_number)}') #4
print(f'2개수: {student_number.count("2")}')  #2 .count가 문자에서 특정문자가 몇개있는지 알려줌
print(f'{"NCT dream darling".upper()}')
print(f'{"NCT dream darling".lower()}')
s="   NCT dream buffering      "
print(f'{s.strip()}')   #strip=벗기다 띄워쓰기가 없어짐
print(f'{s.lstrip()}')  #ls 왼쪽 띄워쓰기가 없어짐
print(f'{s.rstrip()}')  #rs 오른쪽 띄워쓰기가 없어짐
print(f'{s.find("e")}') #[7]
print(f'{s.find("z")}') #없으면 -1
print(f'{s.rfind("e")}') #17
print(f'{s.count("e")}') #2
print(f'{s.index("d")}') #7
# print(f'{s.index("z")}') #없으면 ValueError: substring not found
print(f'{s.replace("buffering", "hello future")}')  #replace하면 원본이 바뀌는게 아니라
print(s)                                            #잠시 바뀐문자열을 return 한다.
#"   NCT dream buffering      "
print('e' in s) #True  특정 문자열안에 e가 있나없나 확인
print('z' in s) #False

#split, join
ip = '10.253.123.119'
ip_List = ip.split('.')
print(ip_List)
names = '양다연, 최자윤, 임채영, 이예진, 인소리'
name_List = names.split(',')
print(name_List)
print(name_List[2])
print(name_List[2:4])
ip_list_str = '::'.join(ip_List)
print(ip_list_str)
name_List_str = ' | '.join(name_List)
print(name_List_str)
print(",".join(name_List))