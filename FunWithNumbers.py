# CS2_Section_Surname_2QFunWithNumbers.py
# "Fun with Numbers" mini app
# This program asks the user for their age
# and calculates the sum of all numbers from 1 up to that age.

print("Hi there! Please enter your age: ", end="")
age = int(input())  # user input

total = 0  # variable to store the sum

# loop to add numbers from 1 up to age
for i in range(1, age + 1):
    total = total + i

# display the result
print("The sum of all numbers from 1 to", age, "is:", total)