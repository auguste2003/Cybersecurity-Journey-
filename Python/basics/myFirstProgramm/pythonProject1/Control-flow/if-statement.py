number = 0

# ternary ifstatement with python 
message = "pisitive" if number > 0 else "0 or negative"

print(message)
if number >0 :
    print(f"The number {number} is greater than 0") #  we must put f at the begining
elif number == 0 :
    print(f"The number {number} is zero")
else:
    print(f"The number {number} is negatif ")

