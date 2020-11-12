#getting user to input data
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