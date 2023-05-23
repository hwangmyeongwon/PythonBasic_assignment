# 예제 #1
Age=int(input("나이를 입력하시오 : "))
if Age>=65:
    print("경로대상입니다.")
else:
    print("경로대상이 아닙니다.")

#예제 #2
num=int(input("정수를 입력하시오 : "))
if num%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#예제:비만 검사
Weight=int(input("무게를 입력하시오:"))
if Weight>=100:
    print("과제충입니다.")
else:
    print("과제충이 아닙니다.")

#연속적인 if-else문
num=int(input("정수를 입력하시오:"))

if num>0:
    print("양수입니다.")
elif num==0:
    print("0입니다.")
else:
    print("음수입니다.")

#난수이용
import random
time=random.randint(1,24)
print("좋은 아침입니다.지금 시각은"+str(time)+"시 입니다.")

sunny=random.choice([True,False])
if sunny:
    print("현재 날씨가 화창합니다.")
else:
    print("현재 날씨가 화창하지 않습니다.")

#종달새가 노래를 할 것인지를 판단해보자.
if time>=6 and time<9 and summy:
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")

#중첩 if-else문
num=int(input("정수를 입력하시오: "))
if num>=0:
    if num==0:
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")

#회원 프로그램
member=123456
M_n=int(input("회원번호를 입력하시오:"))
if M_n==member:
    print("회원님,환영합니다.")
else:
    print("회원이 아니십니다.")

#if문
number=23
guess=int(input('Enter an integer:'))
if (guess==number):
          print('Congratulations,you guessed it.')
          print('(but ypu do not win any prizes)')
elif guess<number:
    print('No, it is a little lower than that')
print('Done')

#예제
number=""
while number!=23:
    number=int(input("숫자를 입력하시오 : "))
print("숫자 일치")

#예제
number=1
sum=0
while (number<=10):
    sum=sum+number
    number=number+1
print("합계는",sum)

#while문
number=23
running=True
while running:
    guess=int(input('Enter an integer:'))
    if guess==number:
        print('Congratulations,you guessed it.')
        running=False
    elif guess<number:
        print('No,it is a little higher than that.')
    else:
        print('No,it is a little lower than that.')
else:
    print('The while loop is over.')
print('Done')


#for 루프
for i in range(1,5):
    print(i)
else:
    print('The for loop is over')

#예제:i의 값 출력
for i in[1,2,3,4,5]:
    print("i=",i)
#예제:i의 값 출력
for i in[1,2,3,4,5]:
    print("9*",i,"=",9*i)

#range() 함수
for i in range(5):
    print("방문을 환영합니다!")
    
#팩토리얼 계산
N=int(input("정수를 입력하시오:"))
Factorial=1
for i in range(1,N+1):
    Factorial=Factoral*i

#break 문

while True:
    s=input('Enter something:')
    if s=='quit':
        break
    print('Length of the string is',len(s))
print('Done')

#continue 문
while True:
    s=input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        print('Too small')
        continue
    print('Input is of sufficient length')








