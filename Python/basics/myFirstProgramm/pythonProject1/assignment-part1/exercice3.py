"""
Exercise 3: Even or Odd

Write a program that asks the user for a number and checks whether it is even or odd. Print an appropriate message.
"""
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Even")
elif a % 2 != 0:
    print("Odd")
