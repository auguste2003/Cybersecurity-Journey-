"""
Exercise 4: Age Check

Write a program that asks the user for their age and prints:
"You are a minor" if the age is less than 18.
"You are an adult" if the age is 18 or more.
"""

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
elif age >= 18:
    print("you are an adult")