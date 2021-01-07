# 내장 함수

# abs
# 절댓값 반환
abs(3)      # 3
abs(-3)     # 3
abs(-1.2)   # 1.2

# all
# 반복 가능한 자료형을 인수로 받아 요소가 모두 참인지 판별
all([1,2,3])    # True
all([1,2,3,0])  # False
all([])         # True

# any
# 반복 가능한 자료형을 인수로 받아 요소 중 참이 있는지 판별
any([1,2,3,0])  # True
any([0,""])     # False
any([])         # True

# chr
# chr(i)는 ASCII 코드 값을 입력받아 해당하는 문자를 출력
chr(97)         # 'a'
chr(48)         # '0'

# dir
# 객체가 자체적으로 가지고 있는 변수나 함수를 출력
dir([1,2,3])    # ['append', 'count', 'extend', 'index', 'insert', 'pop',...]
dir({'1':'a'})  # ['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]

# divmod
# a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
divmod(7,3)     # (2,1)

# enumerate
# 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 반환
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i,name)
# 0 body
# 1 foo
# 2 bar

# eval
# 실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 반환
eval('1+2')         # 3
eval("'hi' + 'a'")  # 'hia
eval('divmod(4,3)') # (1,1)

# hex
# 정수 값을 입력받아 16진수로 변환하여 반환
hex(234)            # '0xea'
hex(3)              # '0x3'

# id
# 객체를 입력받아 객체의 고유 주소 값을 반환
a = 3
id(3)               #135072304
id(a)               #135072304
b = a
id(b)               #135072304

# input
# 사용자 입력을 받는 함수
a = input()

# int
# 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 반환
int('3')            # 3
int(3.4)            # 3
# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 반환
int('11',2)         # 3
int('1A', 16)       # 26

# isinstance
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단
class Person: pass
a = Person()
isinstance(a, Person)       # True
b = 3
isinstance(b, Person)       # False

# len
# len은 입력값의 길이를 반환
len("python")       # 6
len([1,2,3])        # 3
len((1,'a'))        # 2

# list
# 반복 가능한 자료형을 입력받아 리스트로 만들어 반환
list("python")      # ['p','y','t','h','o','n']
list((1,2,3))       # [1,2,3]

# map
# 함수와 반복 가능한 자료형을 입력하 입력받은 자료형의 각 요소를 각 함수가 수행한
# 결과를 묶어서 반환
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

res = two_times([1,2,3,4])
print(res)                          # [2,4,6,8]

def two_times(x):
    return x*2
list(map(two_times, [1,2,3,4]))     # [2,4,6,8]

# max
# 반복 가능한 자료형을 입력받아 최댓값을 반환
max([1,2,3])        # 3
max("python")       # 'y'

# min
# 반복 가능한 자료형을 입력받아 최솟값을 반환
min([1,2,3])        # 1
min("python")       # 'h'

# ord
# 문자의 아스키 코드 값을 반환
ord('a')            # 97
ord('0')            # 48

# round
# 숫자를 입력받아 반올림하여 반환
round(4.6)          # 5
round(4.2)          # 4
round(5.678,2)      # 5,68

# sorted
# 입력값을 정렬한 후 그 결과를 리스트로 반환
sorted([3,1,2])     # [1,2,3]
sorted(['a','c','b']) # ['a','b','c']
sorted("zero")          # ['e','o','r','z']
sorted((3,2,1))         # [1,2,3]

# str
# 문자열 형태로 객체를 변환하여 반환
str(3)      # '3'
str('hi')   # 'hi'
str('hi'.upper())   # 'HI'

# sum
# 리스트나 튜플의 모든 요소의 합을 반환
sum([1,2,3])        # 6
sum([4,5,6])        # 15

# tuple
# 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 반환
tuple("abc")        # ('a','b','c')
tuple([1,2,3])      # (1,2,3)
tuple((1,2,3))      # (1,2,3)

# type
type("abc")         # <class 'str'>
type([])            # <class 'list'>

# zip
# 동일한 개수로 이루어진 자료형을 묶어 주는 역할
list(zip([1,2,3],[4,5,6]))   # [(1,4),(2,5),(3,6)]
list(zip([1,2,3],[4,5,6],[7,8,9]))  # [(1,4,7),(2,5,8),(3,6,9)]
list(zip("abc","def"))      # [('a','d'),('b','e'),('c','f')]
