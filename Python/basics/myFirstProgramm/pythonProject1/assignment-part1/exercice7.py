"""
Exercise 7: List Slicing

Create a list of numbers from 1 to 10.
Slice the list to get:
The first three elements.
The last three elements.
The middle four elements.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:3])
print(numbers[2:])
print(numbers[7:])
print(numbers[::2])
print(numbers[1::2])


# Erstellen einer Liste von 1 bis 10
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Die ersten drei Elemente
erste_drei = zahlen[:3]
print("Erste drei Elemente:", erste_drei)  # Ausgabe: [1, 2, 3]

# Die letzten drei Elemente
letzte_drei = zahlen[-3:]
print("Letzte drei Elemente:", letzte_drei)  # Ausgabe: [8, 9, 10]

# Die mittleren vier Elemente (Elemente 4 bis 7)
mittlere_vier = zahlen[3:7]
print("Mittlere vier Elemente:", mittlere_vier)  # Ausgabe: [4, 5, 6, 7]
