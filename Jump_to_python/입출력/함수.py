# 함수

def add(a,b):
    return a+b

a = 3
b = 4
c = add(a,b)
print(c)        #7

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)        #Hi

# 결과값이 없는 함수
def add(a,b):
    print("{}+{]는 {}입니다.".format(a,b,a+b))

add(3,4)        #3+4는 7입니다.
a = add(3,4)
print(a)        #None

# 입력값과 결과값이 없는 함수
def say():
    print('Hi')

say()           #Hi


# 입력값이 미정일 경우
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

res = add_many(1,2,3)
print(res)              #6

res = add_many(1,2,3,4,5,6,7,8,9,10)
print(res)              #55

# 매개변수 이름 앞에 *를 붙이면 입력값을 전부 모아서 튜플로 만들어 준다
def add_mul(choice,*args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

res = add_mul('add',1,2,3,4,5)
print(res)              #15

res = add_mul('mul',1,2,3,4,5)
print(res)              #120

# 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)       #{'a':1}

print_kwargs(name='foo',age=3)  #{age: 3, name : 'foo'}

# 매개변수 앞에 **를 붙이면 딕셔너리로 만들어진다.

# lambda
add = lambda a,b : a+b
result = add(3,4)
print(result)       #7
