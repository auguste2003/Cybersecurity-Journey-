"""
Exercise 11: Student Score Tracker

Create a program that keeps track of student scores.
Create a list of students, each student being represented as a dictionary with keys: "name", "age", and "scores" (where scores is a list of integers).
Add at least three students to the list.
Calculate and print the average score for each student.
Print the name of the student with the highest average score.
"""
jamal = {
    "name": "Jamal",
    "age": 23,
    "adress": "USA",
    "scores": [90, 90, 90, 90, 90, 90, 90, 90]
}
fred = {
    "name": "fred",
    "age": 21,
    "adress": "Cameroon",
    "scores": [90, 80, 70, 60]
}
cal = {
    "name": "cal",
    "age": 24,
    "adress": "Sami",
    "scores": [90, 90, 90, 90, 90, 90, 90, 90]
}

students = [jamal, fred, cal ]

students.append({
    "name": "alin",
    "age": 23,
    "adress": "Sami",
    "scores": [90, 90, 90, 90, 90, 90, 90, 90]
})
students.append({
    "name": "alin",
    "age": 25,
    "adress": "Sami",
    "scores": [90, 90, 90, 90, 90, 90, 90, 90]
})
students.append({
    "name": "alin",
    "age": 29,
    "adress": "Sami",
    "scores": [90, 90, 90, 90, 90, 90, 90, 90]
})

for student in students:
    print(student)

for student in students:
    print(student["name"] +":", sum(student["scores"]))

best_student = students[0] # the first is at the begining the best
for student in students:
    if student["scores"] > best_student["scores"]: # we have annothe who is tronger
        best_student = student

print("The best student is " +best_student["name"])


print("the correction")
# Step 1: Create a list of students, each represented as a dictionary
students = [
    {"name": "Alice", "age": 20, "scores": [85, 90, 78]},
    {"name": "Bob", "age": 22, "scores": [92, 88, 84]},
    {"name": "Charlie", "age": 19, "scores": [70, 75, 80]}
]

# Step 2: Calculate and print the average score for each student
for student in students:
    name = student["name"]
    scores = student["scores"]
    average_score = sum(scores) / len(scores)
    student["average_score"] = average_score  # Store the average score in the dictionary
    print(f"{name}'s average score is: {average_score:.2f}")

# Step 3: Find and print the name of the student with the highest average score
highest_avg_score = 0
top_student = ""

for student in students:
    if student["average_score"] > highest_avg_score:
        highest_avg_score = student["average_score"]
        top_student = student["name"]

print(f"The student with the highest average score is: {top_student} with an average score of {highest_avg_score:.2f}")
