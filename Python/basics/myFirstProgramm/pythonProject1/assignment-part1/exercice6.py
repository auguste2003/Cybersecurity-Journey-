"""
Exercise 6: List Operations

Create a list named fruits with the following items: "apple", "banana", "cherry", "date", "elderberry".
Do the following:
Print the first and last fruit.
Add a new fruit to the end of the list.
Remove "banana" from the list.
Print the updated list.
"""

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("first fruit: ", fruits[0])
print("last fruit: ", fruits[-1])
fruits.append('apple')
print("updated fruit: ", fruits)
fruits.remove('cherry')
print("updated fruit: ", fruits)