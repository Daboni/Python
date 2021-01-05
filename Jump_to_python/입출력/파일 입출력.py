# 파일 입출력

# 파일 생성
f = open("새파일.txt", 'w')
f.close()

# 파일 쓰기
f = open("새파일.txt", 'w')
for i in range(1,11):
    data ="{}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()


# 프로그램의 외부에 저장된 파일을 읽는 방법

# readline()
# 한 줄 읽기
f = open("C:\Users\jdb44\Desktop\Jump_to_python\입출력\새파일.txt",'r')
line = f.readline()
print(line)
f.close()

# 전체 줄 읽기
f = open("C:\Users\jdb44\Desktop\Jump_to_python\입출력\새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines()
f = open("C:\Users\jdb44\Desktop\Jump_to_python\입출력\새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)

f.close()
# readlines() 는 리스트로 불러옴

# read()
f = open("C:\Users\jdb44\Desktop\Jump_to_python\입출력\새출력.txt",'r')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open("C:\Users\jdb44\Desktop\Jump_to_python\입출력\새출력.txt",'a')
for i in range(11,20):
    data ="{}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()

