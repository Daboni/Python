# dictionary
# 딕셔너리의 key 값에는 변하는 값은 쓸 수 업다.

dic={'name':'pey','phone':'0119993323','birth':'118'}

a = {1:'hi'}
a = {'a':[1,2,3]}

# 추가
a = {1:'a'}
a[2] = 'b'
a               #{1:'a',2:'b'}

a[3] = [1,2,3]
a               #{1:'a',2:'b',3:[1,2,3]}

a['name'] = 'pey
a               #[1:'a',2:'b',3:[1,2,3],'name':'pey'}

# 삭제
del a[1]
a               #{2:'b',3:[1,2,3],'name':'pey'}

# key, value
grade = {'pey':10, 'julliet':99}
grade['pey']        #10
grade['julliet']    #99

a = {'name':'pey','phone':'0119993323','birth':'1118'}
a.keys()            #dict_key(['name','phone','birth'])

# key 리스트 만들기
list(a.keys())

# value 리스트 만들기
a.values()          #dict_values(['pey','0119993323','birth'])

# Key, Value 쌍 얻기
a.items()           #dict_items([('name','pey'),('phone','0119993323'),('birth','1118')])

# clear()
a.clear()
a                   #{}

#get()
a = {'name':'pey','phone':'0119993323','birth':'1118'}
a.get('name')       #'pey'
a.get('phone')      #'0119993323'
a.get('nokey')      #None

# a.get(key)은 a[key]와 다르게 없는 key값을 찾을 때, 거짓의 의미인 None을 반환한다.

# a.get('foo','bar')        #'bar'
# get(x, 디폴트 값)

# Key가 dictionary 안에 존재하는지 조사하기(in)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
'name' in a         #True

'email' in a        #False
