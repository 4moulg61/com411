#printing and using if statements
print("What type of book is this?")
book = input()
#use "in" in order to be able to list strings the user could input
if book in ['Adventure', 'adventure']:
  print("I like adventure books!")
  print("\nFinished reading book.")