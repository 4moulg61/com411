#asking user to input answers
print("What is your name human?")
name = input()

print("How old are you in years?")
age = int(input())

print("How tall are you in meters?")
height = float(input())

print("How much do you weigh in Kilograms?")
weight = float(input())
#rounding numbers using .format
bmi = float(weight / height ** 2)
rounded_bmi = "{:.2f}".format(bmi)
print(name, "you are", age, "and your BMI is", rounded_bmi)