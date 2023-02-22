# list1=[1,2,3,4,5,6,7,8,9,10]
# print(list1)
# for x in list1:
#     print(x)
for x in range(1,11):
    print(x, end=" ")
print("\n")
# print("Odd Num:")
for x in range(1,100):
    if x % 2 != 0:     # condition checks if a number is not divisible by 2 it will print that odd number
        print(x, end=" ")
print("\n")
print("Even Num:")
for x in range(1,100):
    if x % 2 == 0:     # condition checks which number gives remainder 0 then it will print the number
        print(x, end=" ")
print("\n")


for i in range(0, 11):
    print ("%d * %d = %d" % (23, i, 23* i))


for x in range(1,101,2):# The range(2, 101, 2) function generates a sequence of numbers from 1 to 99 in steps of 2
    print(x,end=" ")       # here third value that will hide for every step
print("\n")

for x in range(2,101,2):
    print(x, end=" ")
print("\n")