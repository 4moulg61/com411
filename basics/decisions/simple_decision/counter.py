#asking user for their input
print("Please enter the first whole number")
first_number = int(input())
print("Please enter the second whole number")
second_number = int(input())
print("Please enter the third whole number")
third_number = int(input())
#declaring the integer and making it equal to 0
evens = int = 0
odds = int = 0
#using modulo operator to count
if (first_number % 2 == 0):
 evens = evens + 1
else:
  odds = odds + 1

if (second_number % 2 == 0):
 evens = evens + 1
else:
  odds = odds + 1

if(third_number % 2 == 0):
  evens = evens + 1
else:
  odds= odds +1 

print("There are {} odd numbers and {} even numbers!" .format(odds, evens))

