a=3
print(a ** 3)
#presidence of operators
print(5+8-2)
print(5-8+2)
#String manipulation
str1="welcome"
print(len(str1))
print(str1[2])
a=1234
c=str(a)
print(type(c))
#operations in string #find
print(str1.find("l"))
print(str1.find("a"))
print(str1.upper())
print(str1)
print(str1.count("e")) #count
print(str1.isupper())
str2=" hello "
print(str2)
print(str2.strip()) #removing space
x=" coimbatore "
print(x.replace("o","a").upper()) #replace and uppercase - 2 operations in same line
print(x.lstrip()) #left side space remove
print(x.rstrip()) #right side space remove
#split operation
x1="You can use multiple programming languages like Java, C#, Python, etc to create Selenium Test Scripts"
print(x1.split())
print(x1.split("etc"))
x2="sathish\" kumar" #\" escape character (escape the logic)
print(x2)
x3='''
Selenium Software is not just a single tool
'''
print(x3)
print('not' in x3)
print(x3[::-1])
print(x3.capitalize())