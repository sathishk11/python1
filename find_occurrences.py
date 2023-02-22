# Prompt the user to enter a string
str = input("Enter a string: ")

# Initialize a count variable to keep track of occurrences of "a"
count = 0

# Iterate over each character in the string
for char in str:
    # Check if the current character is equal to "a" or "A"
    if char == 'a' or char == 'A':
        # If so, increment the count variable by 1
        count += 1

# Print out the total count of occurrences of "a"
print("The occurrence of 'a' in the string is:", count)

s="sathish is from namakkal"
mylist = list(s)
print(mylist)
count = 0
for char in mylist:
    count+=char.count('a')

print(count)