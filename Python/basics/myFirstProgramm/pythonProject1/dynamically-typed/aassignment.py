# Step 1: Assigning an integer
a = 100
print(a)  # Output: 100
print(type(a))  # Output: <class 'int'>

# Step 2: Reassigning a string
a = "Dynamic typing in Python"
print(a)  # Output: Dynamic typing in Python
print(type(a))  # Output: <class 'str'>

# Step 3: Reassigning a list
a = [1, 2, 3, 4, 5]
print(a)  # Output: [1, 2, 3, 4, 5]
print(type(a))  # Output: <class 'list'>

# Solution2 : Checking the type

# Step 1: Assigning a float
b = 3.14159
if isinstance(b, float):
    print("b is a float")  # Output: b is a float

# Step 2: Reassigning a boolean
b = True
if isinstance(b, bool):
    print("b is a boolean")  # Output: b is a boolean


# Solution 3 : Type hinting

def multiply(a: int, b: int) -> int:
    return a * b


# Test the function with integers
print(multiply(2, 3))  # Output: 6

# Test the function with different types
print(multiply(2.5, 3))  # Output: 7.5 (Python still executes but the type hint suggests it should be int)
