"""
Exercise 2: Dictionary Iteration

Create a dictionary that stores the names of 5 students as keys and their scores as values.
Use a for loop to print each student's name and score.
Calculate and print the average score.
"""

students = [{"name":"alex","score":34},{"name":"Salva","score":32},{"name":"Lutre","score":66},{"name":"gonza","score":34},{"name":"ningtedem","score":45},]

for student in students:
    print(f"{student['name']}: {student['score']}")

average_score = 0
for student in students:
    average_score += student['score']
print("Average score:", average_score/len(students))