#code to use if and else statements with strings to give a specific response if the user inputs "calculate"
print("Please enter the activity to be performed:")
activity = input()
if (activity in ['calculate', 'Calculate']):
  print("\nPerforming calculations...")
else:
  print("\nPerforming activity...")
print("\nDone!")
