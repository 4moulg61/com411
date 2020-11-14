#beep asks user
print("Where should I look for my battery")
answer1 = str(input())

if(answer1== "in the bedroom"):
  print("Where in the bedroom should I look?")
  answer2 = str(input())
  if(answer2== "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery!")
elif(answer1== "in the bathroom"):
  print("where in the bathroom?")
  answer2 = str(input())
  if(answer2== "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery!")
elif(answer1=="in the lab"):
  print("Where in the lab should I look?")
  answer2 = str(input())
  if(answer2=="on the table"):
    print("Yes I found my battery!")
  else:
    print("Found some tools but no battery")
else:
  print("I dont know where that is but I'll keep looking")