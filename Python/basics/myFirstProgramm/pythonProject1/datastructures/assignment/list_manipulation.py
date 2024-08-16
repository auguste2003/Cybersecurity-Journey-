"""
Exercise 1: List Manipulation

Create a list of numbers from 1 to 20.
Use a for loop to create a new list that contains only the even numbers from the original list.
Print the new list.
"""
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even_list = []
for number in numbers:
    if number % 2 == 0:
        even_list.append(number)
print("number of the list",numbers)
print("even_list",even_list)