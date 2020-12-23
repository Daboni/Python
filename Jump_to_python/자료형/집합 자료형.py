# set
s1 = set([1,2,3])
s1                  #{1,2,3}

s2 = set("Hello")
s2                  #{'e','H','l','o'}

# set은 중복을 허용하지 않고, 순서가 없다(Unordered).
# indexing을 하기 위해선 list나 tuple로 변환해야한다.

s1 = set([1,2,3])
l1 = list(s1)
l1                  #[1,2,3]
l1[0]               #1

s2 = set([1,2,3])
t1 = tuple(s1)
t1                  #(1,2,3)
t1[0]               #1

# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
s1 & s2             #{4,5,6}
s1.intersection(s1) #{4,5,6}

# 합집합
s1 | s2             #{1,2,3,4,5,6,7,8,9}
s1.union(s2)        #{1,2,3,4,5,6,7,8,9}

# 차집합
s1 - s2             #{1,2,3}
s2 - s1             #{8,9,7}

s1.difference(s2)   #{1,2,3}
s2.difference(s1)   #{8,9,7}

# add() 값 1개 추가
s1 = set([1,2,3])
s1.add(4)
s1                  #{1,2,3,4}

# update() 값 여러 개 추가
s1 = set([1,2,3,])
s1.update([4,5,6])
s1                  #{1,2,3,4,5,6}

# remove()
s1 = set([1,2,3])
s1.remove(2)
s1                  #{1,3}
