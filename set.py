
n = {'string',12,13,14}
print(n)
print(type(n))
#print(n[0])
n.add('mister')
print(n)
n.update([2,5,7])
print(n)
n.discard(2)
print(n)
n.remove(12)
print(n)

p = {'12',14,(120,'string','print'),1.0}
print(p)
for i in p:
    print(i)
q = [88,89,80,'string']
s=set(q)
print(s)

n = ['string']
print(n)
s = ('string',)
print(s)

q = {'helloworld'}
print(q)
n = set("helloworld")
print(n)


#how issubset works

a = {1,2,3}
b = {1,2,3,4,5}
c = {1,2,4,5}
print(a.issubset(b))
print(b.issubset(a))
print(a.issubset(c))
print((c.issubset(b)))


# if we want to represent unique values we should use set .
# set is mutable object ,we can change any value in the set according to our requirement
#set doesn't support duplicate values,heterogenous values,indexing and slicing,we cannot sor the elements.

l =[1,30, 30, 40, 33,55,55]
print(l)
n = set(l)
print(n)
s = sorted(n)
print(s)

# important functions of set add,update ,remove, discard,pop, clear
# add function take only one argument as element to set,but update function take multiple arguments to set but all
# all the are iterable objects.




# set cannot have mutable items
t = {12,13,'string',[1,2]}
print(t)'''


s = {10,20, 40}
n = [22,33,44]
s.update(n,range(5))
print(s)

s = input('enter any word :')
p = set(s)
v = {'a','e','i','o','u'}
t = p.intersection(v)
print(t)
