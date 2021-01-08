# 정규 표현식2

# 메타 문자

# 문자 클래스 []
# "[]" 사이의 문자들과 매치

# Dot(.)
# 줄바꿈 문자인 \n을 제외한 모든 문자와 매치

# 반복(*)
# * 바로 앞에 있는 문자가 0부터 무한대로 반복될 수 있다는 의미

# 반복(+)
# + 바로 앞에 있는 문자가 최소 1 이상 반복

# 반복({m,n},?)
# 반복 횟수를 m부터 n까지 매치
# ?는 {0,1}을의미

# 정규식을 이용한 문자열 검색

import re
p = re.compile('[a-z]+')

# match
# 문자열의 처음부터 정규식과 매치되는지 조사

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)            # None

# search
# 문자열 전체를 검색하여 정규식과 매치되는지 조사

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

# findall
# 정규식과 매치되는 모든 문자열을 리스트로 반환

result = p.findall("Life is too short")
print(result)       #["Life","is","too","short"]

# finditer
# 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 반환

result = p.finditer("Life is too short")
print(result)
for i in result: print(i)

# match 객체의 메서드

# group - 매치된 문자열을 반환
# start - 매치된 문자열의 시작 위치를 반환
# end - 매치된 문자열의 끝 위치를 반환
# span - 매치된 문자열의 (시작,끝)에 해당하는 튜플을 반환

m = p.match("python")
m.group()       # 'python'
m.start()       # 0
m.end()         # 6
m.span()        # (0,6)

m = p.search("3 python")
m.group()       # 'python'
m.start()       # 2
m.end()         # 8
m.span()        # (2,8)

# 모듈 단위로 수행하기

p = re.compile('[a-z]+')
m = p.match('python')

m = re.match('[a-z]+','python')

# 컴파일 옵션

# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 함

import re
p = re.compile('a,b')
m = p.match('a\nb')
print(m)        # None

p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)

# IGNORECASE(I) - 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션

p = re.compile['[a-z]', re.I)
p.match('python')
p.match('Python')
p.match('PYTHON')

# MULTILINE(M) - 여러줄과 매치할 수 있도록 하는 옵션

import re
p = re.compile("^python\s\w+")

data = """ python one
life is too short
python two
you need python
python three"""

print(p.findall(data))      # ['python one']

import re
p = re.compile("^python\s\w+",re.MULTILINE)

data = """ python one
life is too short
python two
you need python
python three"""

print(p.findall(data))      # ['python one','python two','python three']

# VERBOSE(X) - verbose 모드를 사용할 수 있도록 하는 옵션

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
 |  [0-9]+          # Decimal form
 |  x[0-9a-fA-F]+   # Hexadecimal form
)
;                   # Trailing semicolon
""", re.VERBOSE)

# 백슬래시 문제
p = re.complie(r'\\section')
# r 문자를 삽입하면 정규식 Raw String 규칙에 의하여 백슬래시 2개 대신 1개만 써도
# 2개를 쓴것과 동일한 의미를 갖게 된다.
