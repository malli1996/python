n=[12,13,11,12,'string',10.20,True,10+5j]
print(n)
print(type(n))
for s in n:
    print(s)
print(n[0])
print(n[0:6])
print(n[0:])
print(n[:7])
print(n[::-1])
print(n[2:8])
print(n[-3:-7])
print(n[:-2])
# nested list
n=[1,2,7,9,[12,23,13],['a']]
print(n)
for t in n:
    print(t)
print(n[0])
print(n[1])
print(n[:])
n[0]=20
print(n)
n[1:4]=3,5,10
print(n)
n.append(200)
print(n)
n.extend([20,30,40])
print(n)
print(['re']*3)
n.insert(2,30)
print(n)
del n[2]
print(n)
del n[1:3]
print(n)
# del n # we got error
# print(n)
n.remove(20)
print(n)
n.pop()
print(n)
n.pop(3)
print(n)
#n.clear()
#print(n)

# finally we also delete items in a list by assigning an empty list to a slice of elements
n[2:3]=[]
print(n)
s=[20,12,23,45,33,44,44]
print(20 in s)
print(44 in s)
print(20 not in s)
s.sort(reverse=True)
print(s)
print(s.count(44 ))

n=[2 ** x for x in range(10) if x%2 ==0]
print(n)
n=[2 ** x for x in range(10) if x > 5]
print(n)
n=[2 ** x for x in range(10) if x % 2 == 1]
print(n)
n=[x for x in range(10) if x % 2 == 1]
print(n)
s = [ x+y for x in ['python ','c '] for y in ['language','programming']]
print(s)

for fruit in ['apple','banana','juice']:
    print('i like ',fruit)


n = [[10,20,30],[40,44,45],[63,34,45]]
print(n)
print(len(n)) # 3
print(len(n[0])) # 3
for i in n: # row wise
   print(i)
# matrix wise
for j in range(len(n)):
    for k in range(len(n[0])):
        print(n[j][k], end = ' ')
    print()

# equal to represents the alias name
# copy represents the cloaning.
'''

s = ['words','apple','fruit']
l = [ i[0:3] for i in s]
print(l)


l = [10,20,30,40]
j = [30,40,50,60]
print(l)
print(j)
for i in l:
    print(i)
for t in j:
    print(t)
t = [i for i in l if i in j]
print(t)


s = 'web applications are very difficult to make '.split()
q= [[i[::-1],len (i) ]for i in s]
print(q)

s = ['a','e','i','o','u']
letter = input('enter any word :')
found = []
for i in letter:
    if i in s:
        if i not in found:
            found.append(i)

print(found)
