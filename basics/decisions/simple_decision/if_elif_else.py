<<<<<<< HEAD
#using elif to provide options and display a suitable response by asking the user to input a direction and displaying the relevant response
print("Towards which direction should I paint (up, down, left or right)?")
direction = input() 

if (direction == "up"):
    print("\nI am painting in the upward direction!")
elif (direction == "down"):
    print("\nI am painting in the downward direction!")
elif (direction == "left"):
    print("\nI am painting in the leftward direction!")
elif (direction == "right"):
    print("\nI am painting in the rightward direction!")
else:
    print("\nI don't know what to do")
=======
#using elif to provide options and display a suitable response
print("Towards which direction should I paint up, down, left or right?")

direction = input()
if (direction == "up", "Up"):
  print("I am painting in the upward direction!")

elif (direction == "down", "Down"):
  print("I am painting in the downward direction!")
elif (direction == "left", "Left"):
  print("I am painting in the left direction!")
elif (direction == "right", "Right"):
  print("I am painting in the right direction!")
else:
  print("I don't know what you mean")
>>>>>>> 8f4de27723890d5e89b379eabc9b0d9cde149efc
