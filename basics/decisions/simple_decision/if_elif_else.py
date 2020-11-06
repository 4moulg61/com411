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