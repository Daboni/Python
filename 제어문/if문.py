# if문
money= True
if money:
    print("택시를 타고 가라")
print("걸어 가라")
# if문
money= True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#택시를 타고가라

# 비교연산자
x = 3
y = 2

x > y           #True

x < y           #False

x == y          #False

x != y          #True

# 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.
money = 2000

if money >= 3000:
    print("택시를 타라")
else:
    print("걸어가라")

# 걸어가라

# and,or,not
# 돈이 3000원 이상이거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라.
money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타라")
else:
    print("걸어 가라")

#택시를 타라


# x in s, x not in s

# in list
1 in [1,2,3]        #True
1 not in [1,2,3]    #False

# in tuple
'a' in ('a','b','c')    #True
'a' not in ('a','b','c')    #False

# in string
'j' not in 'python'     #True

# 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타라")
else:
    print("걸어 가라")

# 택시를 타라

# pass
# 주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라.
pocket = ['paper','money','cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# elif
# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라
pocket = ['paper','handphone']
card = True
if 'money' in pocket:
    print("택시를 타라")
elif 'card' in pocket:
    print("택시를 타라")
else:
    print("걸어 가라")

# 택시를 타라

# conditional expression
message = "success" if score >= 60 else "failure"
