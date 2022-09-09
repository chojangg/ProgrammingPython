#3. 십진수를 2진수로

def dec_to_bin(number):
    s = ''
    #share : 몫, reminder : 나머지
    #무한반복
    while True:
        #number가 0이면, 끝내고 결과 리턴
        if number==0:
            return s
        #아니면, number을 2로 나눈 나머지를 앞으로 보관.
        else:
            reminder = number%2
            s = str(reminder) + s
        #number는 number을 2로 나눈 몫으로 설정한다.
        number = number//2

#def dec_to_bin2(number):
#    return bin(number) [2:]


print(dec_to_bin(10))   #1010
print(dec_to_bin(2))   #10
print(dec_to_bin(77))   #1001101
print(dec_to_bin(1024))   #1000000000