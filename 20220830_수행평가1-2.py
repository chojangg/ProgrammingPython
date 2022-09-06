# 2. 영단어를 인자로 받아, 모음인 a, e, i, o, u만 대체하여 리턴하는 encrypt 함수를 작성하시오.
def encrypt(word):
    result = ''
    # 영단어를 하나씩 꺼내기
    for char in word:
        # 모음인지 구분하기
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            char ='*'
            result += char
        else:
            result += char
    return result

print(encrypt('ive'))   # *v*
print(encrypt('nct dream'))   # nct dr**m
print(encrypt('AEiou'))   # *****
print(encrypt('GOOGLE'))   # G**GL*
print(encrypt('BTS'))   #BTS