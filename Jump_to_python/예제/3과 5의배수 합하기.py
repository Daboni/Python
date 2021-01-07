# 3과 5의 배수 합하기

res = 0
for i in range(3,10001):
    if i % 3 == 0:
        res += i
    elif i % 5 == 0:
        res += i

print(res)
