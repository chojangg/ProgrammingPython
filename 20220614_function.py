# 예약어X
# snake_case
# sum = 0 TypeError: 'int' object is not callable
# def sum(x): # 내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출 불가
#   print(x)
a = sum([10, 20, 3])
print(a)
print('*'*20)
'''
java 함수
접근제어자 리턴형 함수명(파라미터1, 파라미터2){
    return 값;
}
C 함수
리턴형 함수명(파라미터1, 파라미터2){
    return 값;
}

python 함수
def 함수명(파라미터1, 파라미터2):
    return 값
'''
def my_print(age):
    print('choija: ' + str(age) + '살입니다.')     # 이름: 살입니다.
    print('choija: ',age,'살입니다.')       # 이름:  18 살입니다.
    print(f'choija: {age}살입니다.')

def my_print2(name, age):
    print(name +': '+ str(age) + '살입니다.')     # 이름: 살입니다.
    print(name, ':', age,'살입니다.')       # 이름:  18 살입니다.
    print(f'{name}: {age}살입니다.')

print(my_print(18))   # my_print() 실행, my_print()의 리턴값 출력
print(my_print2('안유진',20))   # my_print2() 실행, my_print()의 리턴값 출력
print(my_print2(age=20, name='안유진'))   # 아규먼트 순서와 관계없이 파라미터 이름을 쓰면 거기에 들어감
print('*'*20)

def my_print3(name, age, group):
    print(name +': '+ str(age) + '살입니다.' + group + '소속입니다.')    # 이름: 살입니다.
    print(name, ':', age,'살입니다.', group, '소속입니다.')    # 이름:  18 살입니다.
    print(f'{name}: {age}살입니다. {group} 소속입니다.')

my_print3(age=20, name='안유진', group='아이브')
#my_print3('안유진', age=20, '아이브')     # 키워드 인자 뒤에는 계속 키워드 인자 해야 함
my_print3('안유진', group='아이브', age=20)   # 위치 인자는 무조건 키워드 인자 앞에 있어야 함
print('*'*20)

def my_print4(name, age, group='아이브'):
    print(name +': '+ str(age) + '살입니다.' + group + '소속입니다.')    # 이름: 살입니다.
    print(name, ':', age,'살입니다.', group, '소속입니다.')    # 이름:  18 살입니다.
    print(f'{name}: {age}살입니다. {group} 소속입니다.')
my_print4('안유진', age=20, group='아이즈원')  # 위치 인자는 무조건 키워드 인자 앞에 있어야 함
print('*'*20)

# 가변인자
def my_print5(*args):
    print('정보 : ')
    #print(type(args))
    for arg in args:
        print(arg)
def my_print6(name, *args):
    print('{name}정보 : ')
    #print(type(args))
    for arg in args:
        print(arg)

my_print5('안유진',20,'다이브 ','러브다이브')
my_print6('안유진',20,'다이브 ','러브다이브')
print('-'*20)

# def my_print7(name, age=20, group):   # 기본값 있는 파라미터 뒤에 기본값 없는 파라미터가 올 수 없음
#     print(f'{name}: {age}살입니다. {group} 소속입니다.')
# my_print7('사카타 긴토키', '은혼')
#print('-'*20)
def say(name, msg='안녕하세요', feeling='♡'):
    print(f'{name}, {msg}, {feeling}')
say('가현')
say('가현', '🤍')
say('가현', feeling='🤍')
print('-'*20)
def fn(a, b=[]):
    b.append(a)
    print(b)
fn(3)   # [3]
fn(5)   # [5]:X, [3, 5]
fn(10, [1])# [1, 10]
fn(7)   # [3, 5, 7]
print('-'*20)
say('현진', '미안해')
print('-'*20)
# 지금부터 20년 후의 내 나이 리턴하자
def plus20(age):
    print(age+20)
a = plus20(18)  # 38
print(a)    # None: plus20() return 값이 없어서 None으로 리턴
print('-'*20)
def plus20_2(age):
    return age+20
a = plus20_2(18)  # 38
print(a)
print('-'*20)
# 전화번호 앞 자리(지역번호)와 맨 뒤 네자리 출력하자
def tel(number):
    index = number.find('-')
    f = number[:index]
    b = number[-4:]
    return f, b #(f,b)
# front = '010'
# back = '5678'
front, back = tel('010-1234-5678')
print(f'앞: {front}\t뒤: {back}')
print('-'*20)
# min_max([3, 31, 1, 6, 5, -6])
def min_max(리스트):
    min_value=리스트[0]
    max_value=리스트[0]
    for n in range(1, 6):
        if min_value > 리스트[n]:
            min_value = 리스트[n]
        elif max_value < 리스트[n]:
            max_value = 리스트[n]
    return min_value, max_value

min_value, max_value = min_max([3, 31, 1, 6, 5, -6])
print(f'최소: {min_value}\t최대: {max_value}')

