"""
Exercise 5: Grading System

Write a program that takes a test score as input and prints the grade:
90-100: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"
"""
score = int(input("Enter your score: "))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif score < 60:
    print("F")
