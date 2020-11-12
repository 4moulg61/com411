#asking user to input a number
print("Please enter a whole number")
number = input()

if (number % 2 == 0):
    print("\nThe number {} is an even number.".format(number))
else:
    print("\nThe number {} is an odd number.".format(number))