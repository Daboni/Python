# 4장 문제풀이

# Q1
def is_odd(x):
    if x % 2 == 1:
        print("홀수")
    else:
        print("짝수")

# Q2
def avg(*argv):
    total = 0
    for i in argv:
        total += i
    return total/len(argv)

# Q3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 {}입니다".format(total))

# Q4
print("you" "need" "python")                #youneedpython
print("you"+"need"+"python")                #youneedpython
print("you", "need", "pthon")               #you need python
print("".join(["you","need","python"]))     #youneedpython

# Q5
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt",'r')
print(f2.read())

# Q6
line = input()
f = open("test.txt", 'a')
f.write(line)
f.close()

# Q7
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('jave','python')

f = open("test.txt", 'w')
f.write(body)
f.close()
