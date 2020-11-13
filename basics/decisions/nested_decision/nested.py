#asking what cover the book has
print("What type of cover does the book have, hard or soft?")

cover = str(input())
#nested if statements for soft cover
if (cover== "soft"):
  print("Is it perfect bound?")
  perfect_bound = str(input())
  if (perfect_bound== "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else: 
    print("Soft covers with coils or stitches are great for short books")
#if statements for hard cover
elif (cover =="hard"):
  print("Books with hard covers can be more expensive!")