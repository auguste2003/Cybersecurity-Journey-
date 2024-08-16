"""
Exercise 5: Calculator

Create a function calculator() that takes two numbers and an operator (+, -, *, /) as parameters and returns the result of the operation.
Handle cases where the division by zero might occur and return an appropriate message.

"""
print("do you want ot divide two numbers ?")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operator (+, -, *, /): ")


def calculator(a, b, oparator) -> int:
    if oparator == '+':
        return a + b
    if oparator == '-':
        return a - b
    if oparator == '*':
        return a * b
    if oparator == '/':
        if b == 0:
            print("It is not possible to divide by zero")
        else:
            return a / b


print(calculator(a, b, operation))
