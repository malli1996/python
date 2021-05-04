x=(1,2,3)
print(x)
print(type(x))
n=1,2,"yes"
print(n)
print(type(n))
t=(33,44,"string",[12,13,11])
t[3][2] = 88
print(t)
x=("hello")
print(x)
print(type(x))
y=("hello",)
print(y)
print(type(y))
z=("hello",1,22,20.3,True,5+6J)
print(z)
print(z[0])
print(z[1:4])
print(z[:])
print(z[-1])

for i in z:
    print(i)

#tuple unpacking
a,b,c,d,e,f = z
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


string = ('p','q','r','s','t')
print(string)
print('p' in string)
print('r' in string)
print('z' not in string)
print(string.index('s'))
print(string.count('t'))

market = ('fruits','apple','banana','cake')
for price in market:
    print(price,'very expensive product')
# multiplication
multiply = (('apple') * 3)
print(multiply)

#concatination
a = (1,2,3)
b = (4,5,7)
print(a+b)

s = (88,99,100,[34,88])
print(s)
print(s[3][1])

s = ('string','number','one')
d = list(s)
print(d )
del s
print(s) '''

#tuple :- if our data is fixed then we should go for tuple object
# important functions of tuple is :- index,len,count,sorted.
t =(10,30,40,50)
n = sorted(t,reverse=False)
print(n)

# we can create a tuple by packing group of variables
a = 10
b = 20 # tuple packing.
c = 30
d = 40
t = a,b,c,d
print(t)

# tuple unpacking
t =(10, 40, 50, 60 ,70)
s,b,c,d,f = t
print(s)
print(b)
print(c)
print(d)
print(f)

s = (2 ** x for x in range(1,6))
print(s)
print(type(s))
for i in s:
    print(i)


#print tuple elements sum and its average.
s = (10,20,40)
n = len(s)
print(n)
sum = 0
for x in s:
    sum = sum+x

print('sum is :', sum)
print("average is :",sum/n)

# in both cased list and tuple are same in insertion order , duplicate values allowed,heterogenous values allowed,
# indexing and slicing also same.
# list object cannot use key in dictionary because its hashable and mutable
# tuple object can use as key to the dictionary
