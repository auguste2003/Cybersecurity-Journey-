def greet(name, age):
    print(f"Hello {name} World!")
    if not age < 0:  # check that the age is begger than 0
        print(f"Your age is {age}")


# call the function
greet("Jamila", 12)
greet("Piere", 3)
