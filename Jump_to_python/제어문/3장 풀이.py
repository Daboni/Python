# 연습문제

# Q1
a = "Life is  too short,you need python
if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in :; print("shirt")
elif "need" in a: print("need")
else: print("none")
# shirt

# Q2
# while문을 사용해 1부터 1000까지 자연수 중 3의 배수의 합을 구해보자
i = 1
res = 0
while(i<=1000):
    if i%3 == 0:
        res += i
    i += 1

# Q3
i = 1;
a = '*'
while(i<6):
    print(a*i)
    i += 1

# Q4
# for문을 사용해 1부터 100까지의 숫자를 출력해보자
for i in range(1,101):
    print(i)

# Q5
a = [70,60,55,75,95,90,80,80,85,100]
# 평균을 구하시오

res = 0
for score in a:
    res += score
print(res/len(a))

# Q6
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 ==1:
        result.append(n*2)
#위 코드를 list comprehension을 사용하여 표현해 보자

result = [n%2 for n  in numbers if n%2==1]
