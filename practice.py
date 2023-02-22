# a=int(input('enter the numer'))   #input statement
# print(a*2)
# print(type(a))
#Arithmatic operations
# a=int(input("enter the a value:"))
# b=int(input("enter the b value:"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) # it will return the float value
# print(a//b) # it will return the integer value, it removes the value after .
# print(a%b) # it will return the remaining
#Relational operators <, >, >=, <=, ==
# print(a>b)
#Augumented assignment operators *=, +=, -=, /=
# a=10
# a+=2  # a=a+2
# print(a)
# b=a**5
# print(b)
# a%=b
# print(a)
#Logical operators and or not
# a=10>4 and 30>12 # true and true = true, true and false = false, false and false = false
# print(a)
# b=10>4 or 30<12 # true or true = true, true or false = true, false or false = false
# print(b)
# c=not 30>12 # it negotiate the value, if u give not true answer is false
# print(c)
# print(20%10 == 0 or 30%20 == 0) # answer is true because one condition is true
#Conditional statements
def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)