# 정규 표현식3

# 메타문자

# |
# or과 동일한 의미로 사용

import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# ^
# 문자열의 맨 처음과 일치함을 의미

print(re.search('^Life','Life is too short'))
print(re.search('^Life','My Life'))     #None

# $
# 문자열의 끝과 매치함을 의미

print(re.search('short$', 'Life is too short'))
print(re.search('short&', 'Life is too short, you need python'))    #None

# \A
# 문자열의 처음과 매치됨을 의미(re.MULTILINE에서는 ^과는 다르게 전체 문자열의 처하고만 매치

# \Z
# 문자열의 끝과 매치됨을 의미(\A와 반대)

# \b
# 단어 구분자(Word boundary), 보통 단어는 whitesapce에 의해 구분

p = re.compiler(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))       #None
print(p.search('one subclass is'))      #None
# 반드세 r을 이용하여  Raw string임을 알려줘야 함

# \B
# Wb와 반대로 whitespace로 구분된 단어가 아닌 경우 매치

p = re.compiler(r'\Bclass\B')
print(p.search('no class at all'))      #None
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))      #None

# 그루핑(Grouping)
# 반복되는지 조사
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())        # ABCABCABC

# 찾을 문자열을 조사
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

p = re.compile(r"(\w)+\s+\d+[-]\d+[-]\d+[-]\d+")
m = p.search('park 010-1234-1234')
print(m.group(1))       # park

# group(0) 매치된 전체 문자열
# group(n) n 번째 그룹에 해당하는 문자열

p = re.comile(r"(\w)+\s+(\d)+[-]\d+[-]\d+[-]\d+")
m = p.search('park 010-1234-1234')
print(m.group(2))       # 010

p = re.comiler(r"(\w)+\s+((\d)+[-]\d+[-]\d+[-]\d)+")
m = p.search('park 010-1234-1234')
print(m.group(3))       # 010
# 바깥족 그룹부터 시작하여 안쪽으로 들어갈수록 인덱스 증가

# 그루핑된 문자열 재참조(Backreferences)

p =re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()     # 'the the'
# \1은 앞에 그룹을 재참조하는 메타 문자
# 두 번째 그룹을참조하려면 \2를 사용

# 그루핑된 문자열에 이름 붙이기
# (?P<그룹명>...)

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))          # park

p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
p.search('Paris in the the spring').group()     # 'the the'

# 전방 탐색

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())        # 'http:'

# (?=...) - 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않음
# (?!...) - 해당되는 정규식과 매치되지 않아야하며 조건이 통과되어도 문자열이 소비되지 않음

# 긍정형 전방 탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())        # 'http'

# 부정형 전방 탐색

p = re.compile(".*[.](?!bat$).*$")
# 확장자가 bat이 아닌 경우에만 통과

# 문자열 바꾸기

p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')     #'colour socks and colour shoes'

p.sub('colour', 'blue socks and red shoes', count =1)
#'colour socks and red shoes'

# subn - sub와 기능은 같으나 변경된 문자열과 바꾸기가 발생한 횟수를 나타내는 튜플을 반환
p = re.compile('(blue|white|red)')
p.subn('colour', 'blue socks and red shoes')
#('colour socks and colour shoes', 2)

# 메서드 사용 시  참조 구문 사용하기

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \gName>", "park 010-1234-1234"))
# 010-1234-1234 park

p = re.compile(r"(?}<name>\w+)|s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
# 010-1234-1234 park

# sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
#'Call 0xffd2 for prinring, 0xc000 for user code.'

# Greedy vs Non-Greedy

s = '<html><heal><title>Title</title>'
len(s)      # 32
print(re.match('<.*>', s).span())   # (0, 32)
print(re.match('<.*>', s).group())  # <html><head><title>Title</title>

print(re.match('<.*?>', s).group())     # <html>
# ?는 가능한 한 최소한의 반복을 수행하도록 한다
# ex) *?, +?, ??, {m,n}?
