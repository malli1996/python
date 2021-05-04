s = dict()
print(s)
print(type(s))
s['pthon'] = 'programing'
s['ava'] = 'programing'
s['oracle'] = 'database'
s['seleniun'] = 'testing'
print(s)
print(s['pthon'])
s[('string',)] = 'tuple'
print(s)
t = {'string':'datatype',0:1,1:2,2:3,4:5}
print(t.get(0))
print(t.get(33))
print(t.get(33,39))
print(t.keys())
print(t.values())
print(t.items())