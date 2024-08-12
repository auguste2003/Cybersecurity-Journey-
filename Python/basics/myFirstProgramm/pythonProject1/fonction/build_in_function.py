def is_adult(age):
    if age >= 16:
        return True
    else:
        return False


# define the first function
def convert_gender(gender="Unknow") -> str:
    if gender == "Male":
        return "Male"
    elif gender == "Female":
        return "Female"
    else:
        return "Unknown"


# call the fonction and store the return value
result = is_adult(12)
print(str(result))

print(convert_gender(gender="Male"))
print(convert_gender(gender="Female"))
print(convert_gender(gender="Alain"))
