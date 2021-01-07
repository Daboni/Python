# 간단한 메모장 만들기

import sys

mode = sys.argv[1]
memo = sys.argv[2]

if mode == '-a':
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()

elif mode == '-v':
    f = open('memo.txt','r')
    memo = f.read()
    f.close()
    print(memo)

