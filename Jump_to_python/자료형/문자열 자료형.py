#문자열
"Life is too short, You need Python"
"a"
"123"

# ""
"Hello World"

# ''

'Python is fun'

# """ """
"""Life is too short, You need Python"""

# ''' '''
'''Life is too short, You need Python'''

# ' 포함시키기
food = "Python's favorite food is perl"
food    #"Python's favorite food is perl"


# " 포함시키기
say = '"Python is very easy." he says.'
say     #'"Python is very easy." he says.'

# \이용해서 '," 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# \n 삽입으로 줄 바꾸기
multiline = "Life is too short\nYou need python"

# 연속된 ''' 또는 """ 사용하기
multiline = '''
Life is too short
You need python
'''

multiline = """
Life is too short
You need python
"""

# concatenation
head = "Python"
tail = "is fun!"
head + tail     #'Python is fun!'

# 문자열 곱하기
a = "python"
a * 2           #'pythonpython'

# 문자열 길이
a = "Life is too short"
len(a)          #17

# Indexing and Slicing

# Indexing
a = "Life is too short, You need Python"
a[3]            #'e'

a[-1]           #'n'
a[-2]           #'o'
a[-0]           #'L'

# Slicing
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b               #'Life'

a[0:3]          #'Lif'

a[0:5]          #'Life '
a[0:4]          #'Life'

a[19:]          #'You need Python'
a[:]            #'Life is too short, You need Python'

a[19:-7]        #'You need'

# Slicing 으로 문자열 나누기
a = "20201217Rainy"
date = a[:8]
weather = a[8:]
date            #'20201217'
weather         #'Rainy'

year = a[:4]
day = a[4:8]

year            #'2020'
day             #'1217'

# 문자열 바꾸기
# python에서 문자열의 요솟값은 바꿀 수 없음(immutable한 자료형)
a = "Pithon"
a[:1]           #'P'
a[2:]           #'thon'
a[:1] + 'y' + a[2:] #'Pyhon'

# 문자열 formatting

# 숫자 바로 대입
"I eat %d apples." %3
'I eat 3 apples.'

# 문자열 바로 대입
"I eat %s apples." %"five"
'I eat fieve apples.'

# 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." %number
'I eat 3 apples.'

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)
'I ate 10 apples. so I was sick for three days.'

# %s 는 모든 형태의 값이든 문자열로 자동으로 변환시켜준다.
# %d와 %를 같이 쓸 때 %%를 쓴다.
"Error is %d%%" %98
'Error is 98%'

# 정렬과 공백
"%10s" %"hi"
'        hi'
"-10sjane." %'hi'
'hi   jane.'

# 소수점 표현
"%0.4f" %3.42134234
'3.4213'

"%10.4f" %3.42134234
'    3.4213'

# format 함수를 사용한 formatting

# 숫자 바로 대입
"I eat {} apples".format(3)
'I eat 3 apples'

# 문자열 바로 대입
"I eat {} apples".format("five")
'I eat five apples'

# 숫자 값을 가진 변수로 대입
number = 3
"I eat {} apples".format(number)
'I eat 3 apples'

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {} apples. so I was sick for {} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'

# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3)
'I ate 10 apples. so I was sick for 3 days.'

# 왼쪽 정렬
"{0:<10}".format("hi")
'hi        '

# 오른쪽 정렬
"{0:>10}".format("hi")
'        hi'

# 가운데 정렬
"{0:^10}".format("hi")
'    hi    '

# 공백 채우기
"{0:=^10}".format("hi")
'====hi===='
"{0:!<10}".format("hi")
'hi!!!!!!!!'

# f문자열 formatting
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동 입니다. 나이는 30입니다.'

f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'

# count()
a = "hobby"
a.count('b')        #2

# find()
a = "Python is the best choice"
a.find('b')         #14
a.find('k')         #-1

# index()
a = "Life is too short"
a.index('t')        #8
## index()함수는 없는 문자를 찾으면 오류 발생

#join()
",".join('abcd')
'a,b,c,d'

#upper()
a = "hi"
a.upper()           #'HI'

#lower()
a = "HI"
a.lower()           #'hi'

#lstrip()
a = " hi "
a.lstrip()          #'hi '

#rstrip()
a = " hi "
a.rstrip()          #' hi'

#strip()
a = " hi "
a.strip()           #'hi'

#replace()
a = "Life is too short"
a.replace("Life", "Your leg")       #'Your leg too short'

#split()
a = "Life is too short"
a.split()                           #['Life','is','too','short']
b = "a:b:c:d"
b.split(':')                        #['a','b','c','d']


