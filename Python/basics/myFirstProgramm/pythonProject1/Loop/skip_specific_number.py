"""
Write a program that prints numbers from 1 to 10.
Use continue to skip the number 5.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number == 5:  # skip the number 5
        continue
    print(number)