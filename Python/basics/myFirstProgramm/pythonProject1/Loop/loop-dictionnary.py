person = {
    "name": "Jamal",
    "age": 23,
    "adress": "USA"
}
# key is just a value in person
for key in person:
    print(f"key:{key} value:{person[key]}")
# item represents a line in person
for key, value in person.items():
    print(f"key:{key} value:{value}")

