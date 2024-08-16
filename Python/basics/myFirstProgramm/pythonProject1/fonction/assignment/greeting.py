"""
Write a function greet_user(name) that takes a name as a parameter and prints a greeting. If no name is provided, it should greet "Guest" by default.
"""


def greet_user(name="Guest"):
    print(f"Hello {name}")


greet_user("Bob")  # Output: Hello, Bob!
greet_user("Charlie")  # Output: Hello, Charlie!
greet_user()  # Output: Hello, Guest!
