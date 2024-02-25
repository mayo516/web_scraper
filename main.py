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

