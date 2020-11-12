#ask for user input on a main menu
print("Which task would you like Beep to carry out? \n A- Calculate BMI\n B- Learn your name\n C- Create a self portrait\n D- Change Stats")
answer = str(input())
if answer == "a" or answer == "A":
  #use string operators and data types to display bmi
  print("You have chosen to calculate your BMI\nPlease enter your weight")
  weight= float(input())
  print("\nPlease enter your height")
  height= float(input())
  bmi= float(weight/ height ** 2)
  print("Your BMI is {:.2}".format(bmi))
elif answer == "b" or answer == "B":
  print("What is your name, Human?")
  name = str(input())
  print("Your name is {}".format (name))
elif answer == "c" or answer== "C":
  print("I am going to create a self portrait, what character should my eyes be?")
  eye = input()
  print("Beep's expression is as follows:")
  print("    _______ ")
  print("   / _____ \    ")
  print("  | |" + eye + "___" + eye + "| | ")
  print("   \_______/ ")
  print("       |    ")
  print("      /\ ")
elif answer == "d" or answer == "D":
  print("Please enter the number of lives:")
  lives = int(input())
  print("\nPlease enter the energy level")
  energy = int(input())
  print("\nPlease enter the shield level")
  shield = int(input())

  # display the user input using string operators
  print("\nHealth has been set.")
  print("\nLives:" , "♥" * lives)
  print("\nEnergy:", "♦" * energy)
  print("\nShield:", "♦" * shield)
else:
  print("I do not understand what you have input, Goodbye")