# Exercise 1: Numeric Types

num_int = 42
num_float = 3.14
num_complex = 2 + 3j

print(type(num_int))     # <class 'int'>
print(type(num_float))   # <class 'float'>
print(type(num_complex)) # <class 'complex'>
# Exercise 2: Text Type

greeting = "Hello, Python!"
print(greeting)
print(type(greeting))  # <class 'str'>

multiline_str = """This is a
multi-line string."""
print(multiline_str)
print(type(multiline_str))  # <class 'str'>
# Exercise 3: Sequence Types

fruits = ["apple", "banana", "cherry"]
numbers_tuple = (1, 2, 3)
range_numbers = range(1, 6)

print(fruits)
print(type(fruits))  # <class 'list'>

print(numbers_tuple)
print(type(numbers_tuple))  # <class 'tuple'>

print(range_numbers)
print(type(range_numbers))  # <class 'range'>
# Exercise 4: Mapping Type

book = {
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2021
}

print(book)
print(type(book))  # <class 'dict'>
# Exercise 5: Set Types

unique_nums = {1, 2, 3}
frozen_nums = frozenset([1, 2, 3, 4, 5])

print(unique_nums)
print(type(unique_nums))  # <class 'set'>

print(frozen_nums)
print(type(frozen_nums))  # <class 'frozenset'>
# Exercise 6: Boolean Type

is_active = True
is_inactive = False

print(is_active)
print(type(is_active))  # <class 'bool'>

print(is_inactive)
print(type(is_inactive))  # <class 'bool'>