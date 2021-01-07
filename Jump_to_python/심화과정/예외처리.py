# 예외 처리

# try, except
try:
    4/0
except ZeroDivisionError as e:
    print(e)                        # division by zero

# try ... finally
f = open('foo.txt','w')
try:
    # 무언가를 수행한다.
finally:
    f.close()

# 여러개의 오류처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

# 오류 회피하기
try:
    f =  open("없는파일",'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
# raise 명령어를 통하여 가능
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

# eagle = Eagle()
# eagle.fly()       # 'NotImplementedError'

class Eagle(Bird):
    def fly(self):
        print('very fast')

eagle = Eagle()
eagle.fly()         # 'very fast'
 
