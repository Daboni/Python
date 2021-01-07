# 구구단

def GuGu(n):
    res = [x for x in range(1,10)]
    res = list(map(lambda x: x*n, res))
    print(res)

n = int(input())

GuGu(n)
