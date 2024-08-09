number = 1
number_two = 2
number_three = 3
numbers = [number , number_two, number_three]
print(numbers[0])

# methodes with lists
numbers.sort() # [1, 2, 3]
numbers.reverse() # [3, 2, 1]
print(len(numbers)) # the length of the list
#  numbers.clear() # []
numbers.append(1000)  # [3, 2, 1, 1000]
print(numbers)

print(4 in numbers)




# delete a number from the list
numbers.remove(1)
print("After removing 1 ", numbers)

print("After removing 1 " + str(numbers))
numbers.pop(0) # remove the last one
print("After poping  ", numbers)

del numbers[0]
print(f"After del {numbers[0]} ", numbers)

del numbers[0:1] # remove from index 0 to index 3
print(f"After del ", numbers)