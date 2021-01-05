#for
test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

# 3 7 11

# continue
marks = [90,25,67,45,80]
#6점 이상인 사람에게 축하 메시지를 보내보자.

number=0
for mark in marks:
    number += 1
    if mark >= 60:
        print('{}번 학생은 합격입니다. 축하합니다.'.format(number))
    else :
        continue


# range
a = range(10)   #range(0,10)
a = range(1,11) #range(1,11)

add = 0
for i in range(1,11):
    add += i

# 55

# List comprehension
a = [1,2,3,4]
result = []
for num in a:
    result.append(3*num)
print(result)
#[3,6,9,12]

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
#[3,6,9,12]

a = [1,2,3,4]
result = [num*3 for num in a if num%2==0]
print(result)
#[6,12]

##[표현식 for 항목 in 반복가능객체 if 조건문]

