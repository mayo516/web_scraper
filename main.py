
from random import randint
print("Hello World")

a = 2
b = 3
c = a + b
c = 11
print(c)

my_age = 88

my_name = "eunha"
my_name = 'eunha2'
my_age = "29"
print(my_age)

is_true = True

print(is_true)

print("안녕하세요 저는", my_name, "이고", my_age, "살 입니다!")

def say_hello(name = '익명아'): 
    print("안녕", name )

say_hello("야")
say_hello("은하") 
say_hello("야")
say_hello(2)
say_hello()

#함수만들기 테스트 

def plus(a = 0, b = 0):
    print(a + b)

def minus(a = 0, b = 0):
    print(a - b)

def divide(a = 0, b = 1):
    print(a / b)

def multiply(a = 0, b = 0):
    print(a * b)

#return

def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("지불 감사합니다", tax, '원')

pay_tax(tax_calc(10000))

my_name = "mayo"
my_age = 10
my_color_eyes = "brown"

print(f"hello I'm {my_name}, {my_age}살이야 ㅋㅋ")


#조건문
if 10 == 5 : 
    print("참입니다")
elif 10 == 10:
    print("엘이프")
else:
    print("거짓입니다")


# age = int(input("How old are you?"))

# if age < 19 : 
#     print("술먹으면안돼")
# elif age > 19 and age < 60:
#     print("엘이프")
# else:
#     print("금주하세요")

#파이썬 카지노?
    
# user_choice = int(input('숫자를 선택하세요')) 

# answer = randint(1,100) #라이브러리 import해야함

# if user_choice == answer : 
#     print("정답!")
# elif user_choice < answer:
#     print("정답은 더 큽니다")
# else:
#     print("정답은 더 작습니다")


# user_bbang = input('Q. 은경님이 좋아하는 빵은?')

# if user_bbang: 
#     print("정답입니다!!!!")

# answer = randint(1,100) #라이브러리 import해야함
#파이썬 카지노?
    
user_choice = int(input('숫자를 선택하세요')) 
playing = True
answer = randint(1,100) #라이브러리 import해야함
while playing : 
    user_choice = int(input('숫자를 선택하세요')) 
    if user_choice == answer : 
        print("정답!")
        playing = False
    elif user_choice < answer:
        print("정답은 더 큽니다")
    else:
        print("정답은 더 작습니다")

