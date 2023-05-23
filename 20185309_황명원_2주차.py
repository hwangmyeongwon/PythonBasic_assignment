
#스크립트 모드

def Data_Read():
    data=ser.read(5)
    data_len=numpy.arange(len(data))
    #print(data_len)
num_list=[]
b=[]
for i in data_len:
    #a=str(data[i]-48)
    a=int(data[i].encode('hex'),16)*50/adc_res
    b.append(a)

#문자열
print("안녕하세요?)

#print() 함수
print("결과값은",2*7,"입니다.")

#리터럴 상수: 문자열 포맷팅(3)
age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(name, age))
print ('Why is {} playing with that python?'.format(name) )

#리터럴 상수: 문자열 포맷팅(4)
print('{0:.3f}'.format(1.0/3))
print('{1:.3f}'.format(1.0/3,5.21))

#리터럴 상수:문자열 포맷팅(4)
print ('{name} wrote {book}'.format(name='Swaroop‘,book='A Byte of Python'))

#리터럴 상수:문자열 포맷팅(4)
print( '{1:.3f}'.format(1.0/3,5.21));print( '{0:.3f}'.format(1.0/3))

#리터럴 상수:이스케이프(Escape)문자(1)
print ("What\'s your name?")
print('\t This is the first line \t This is the second line')
print('This is the first line\nThis is the second line')
print("This is the first sentence. \
 ...This is the second sentence.")

#리터럴 상수:순문자열
print(r"Newlines are indicated by \n")

#변수
x=100
y=20
s=x+y

#변수값 변경
x=100
x=200
print(x)

#변수의 사용 :계산
x = 100
y = 200
sum = x + y
print(sum)
                                    
#예제: 변수와 리터럴 상수 사용하기
i =5
print(i)
i = i+ 1
print (i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)

#키보드 입력
x=int(input("첫 번째 정수를 입력하시오:"))

#완전한 코드
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))
product = x * y
print(x, “와", y, "의 곱은", product, "입니다.")

#논리적 물리적 명령행
i=5;print(i);

#명시적 행간 결합
s='This is a string. \ This continues the string'

#들여쓰기
i=5
print('Value is',i)
print('I repeat,the value is',I)

#계산하기
print(3+4)
print(7-4)
print(7*5)
print(8/5)

#문자열과 숫자
print("100"+"200")
print(100+200)
print("송성호"*3)
