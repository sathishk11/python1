# list operations
a=[1,3,6,9,3,5,7]
a.append(10)
print(a)
a.remove(6)
print(a)
print(a.count(3))
a.sort() # sort the values in ascending order
print(a)
print("maximum value is:",max(a)) # it will print the maximum value
print("minimum value is:",min(a)) # it will print the minimum value
print("sum of a is:",sum(a)) # it will print the sum of list
print(abs(len(a))) # it will print the absolute length of list
a.pop(2)
print(a) # it removes the index value of 2
a.pop()
print(a) # it removes the last index
print(3 in a) # it will print the statement is true or false
b=[21,22,23]
c=zip(a,b)
print(list(c))
print(tuple(c))

for i in range(10):
    print(i,end=" ")
# set operators{}
print("\n")
s={50,30,44,76,"A", "M", "M"} # no duplicates are allowed
print(s)
print(len(s))
print(30 in s)
s.add(121)
print(s)
s.pop() # set pop operator removes the index value randomly
print(s)
s.pop()
print(s)
l={12,43,78,34,54}
r={21,43,68, 27}
z=l.union(r)
print(z)
x=l.symmetric_difference(r)
print(x)
y={12,43}
print(y.issubset(l)) #compare the value of y and l
y1={12,33}
print(y1.issubset(l))
y2={43,68}
print(r.issuperset(y2))
y.discard(12)
print(y)
