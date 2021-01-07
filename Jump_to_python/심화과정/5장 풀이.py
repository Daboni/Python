# 5장 풀이

# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)     #10
cal.minus(7)    #3

print(cal.value)    #3

# Q2
class MaxLimitCalculator(Calculator):
    def add(self,value):
        self.value += value
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)     #50
cal.add(60)     #110

print(cal.value) #100

# Q3
all([1,2,abs(-3)-3])    # False
chr(ord('a')) == 'a'    # True

# Q4
list(filter(lambda x:x>0, [1,-2,3,-5,8,-3]))    #[1,3,8]

# Q5
int('0xea',16)      #234

# Q6
list(map(lambda x:x*3, [1,2,3,4]))   #[3,6,9,12]

# Q7
a = [-8,2,7,5,-3,5,0,1]
res = max(a)+min(a)     #-1

# Q8
round(17/3,4)           #5.6667

# Q9
import sys
a = sys.argv[1:]

res = 0
for n in a:
    res += int(n)
    
print(res)

# Q10
import os
os.chdir('C:\\doit')
res = os.popen("dir")
print(res.read())

# Q11
import glob
glob.glob("c:\\doit\\*.py")

# Q12
import time
time.strftime("%Y/%m/%d %H:%M:%S")

# Q13
import random
lotto = [x for x in range(1,46)]
res = []
for i in range(6):
    x = random.choice(lotto)
    lotto.remove(x)
    res.append(x)

