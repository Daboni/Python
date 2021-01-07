# module

# mod1.py
"""
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

"""

import mod1

print(mod1.add(3,4))        # 7
print(mod1.sub(4,2))        # 2

from mod1 import add
add(3,4)                    # 7

# if __name__ = "__main__"
# 직접 파일을 실행했을 때는 참이 되고 대화영 인터프리터나 다른 파일에서
# 모듈을 불러서 사용하면 거짓이 된다.

