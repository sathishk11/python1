# x=5
# y=10
# print(x+y)
# a=10
# b=15
# print(a+b)

def t1(x,y):
    print(x+y)

t1(20,30)

def s(a,b,c):
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    return a**2

z=s(1,2,3)
print(z)


def f1(a):
    x,y=0,1
    for i in range(a):
        print(x,end=" ")
        x,y = y, x+y
f1(15)

print("\n")
x=0
y=1
print(x,y)
x=y
y=x+y
print(x,y)
print("\n")
def f2(a):
    for i in range(-1,15):
        i=i+1
        print(i,end=" ")

f2(10)

# positional arguments
# keyword arguments
# required arguments
# optional arguments