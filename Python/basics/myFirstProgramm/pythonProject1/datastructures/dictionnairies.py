# key and value and keys must be unique
person = {
    "name": "Jamal",
    "age": 23,
    "adress": "USA"
}
print(person)
print(person["name"])
print(person["age"])
print(person["adress"])
print(person.keys()) # all keys
print(person.values()) # all values

print(person.items())
print(person.get("name"))

person.update({"name": "Dorsal"})
print(person.get("name"))
person["name"] = "Dorsalis"
print(person.get("name"))
