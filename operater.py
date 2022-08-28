#Arithmetic operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators

#arithmatic operater
a=3
b=2
c=4
d=a+b
e=a*b
f=a-b
g=a/b
print(d)
print(e)
print(f)
print(g)

#assigment operater
x = 5
x += 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x >>= 3
print(x)

#comparison operator
x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 6
print(x < y)

#logical operator
x = 5
print(x > 3 and x < 10)

x = 8
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

#identify operator
x = ["apple", "banana"]
y = ["apple", "banana","mango"]
z = x

print(x is z)
print(x is y)
print(x == y)

