#연습문제

#Q1 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
# 80, 75, 55

print((80+75+55)/3)

#Q2 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.

print(bool(13%2-1))

#Q3 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

num = '881120-1068234'

print(num[:6])
print(num[6:])

#Q4 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.

pin = '881120-1068234'

print(pin[7])

#Q5 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

a = "a:b:c:d"

b=a.replace(':','#')
print(b)

#Q6 [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

a = [1,3,5,4,2]

a.sort()
a.reverse()

#Q7 ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.

a = ['Life','is','too','short']

b = " ".join(a)
print(b)

#Q8 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.

a = (1,2,3)
b = 4,
c = a + b
print(c)


#10 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.

a = {'A':90, 'B':80, 'C':70}

print(a.pop('B'))

#Q11 a 리스트에서 중복 숫자를 제거해 보자.

a = [1,1,1,2,2,3,3,3,4,4,5]

a = set(a)
