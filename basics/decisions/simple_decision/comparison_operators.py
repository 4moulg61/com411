#asking the user to input a number
print("Please enter the first number:")
number_one = int(input())
print("\nPlease enter the second number:")
number_two = int(input())
#using if to work out and display the output
if (number_one > number_two):
  print("The second number is the smallest!")
elif (number_one < number_two):
  print("The first number is the smallest!")
elif (number_one == number_two):
  print("Both are equal!")
