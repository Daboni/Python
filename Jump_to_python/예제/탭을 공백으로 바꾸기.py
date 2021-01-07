# 탭을 4개의 공백으로 바꾸기

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src,'r')
data = f.read()
f.close()
data = data.replace('\t',' '*4)

f = open(dst, 'w')
f.write(data)
f.close()

