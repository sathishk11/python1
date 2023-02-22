#methods in tuples, tupple is declared in a () brackets
#count
l=(12,43,78,12,34,54) #tuple declaration
print(l.count(12))
print(l.count(43))
print('hello','world',sep='_')
for i in l:
    print(i,end='\t') # \t means tab space between strings

print(type(l))
a=(2,4,6,8)
z=l+a
print(z)
print(a*3) # it will print 3 times of "a" value - string replication
print(a[2]) # it will print the index value of a
print("*")
print("*","*")
print("*","*","*")
str1 = 'code'
str2 = 'io'
print(str1,'.',sep='',end='')
print(str2)