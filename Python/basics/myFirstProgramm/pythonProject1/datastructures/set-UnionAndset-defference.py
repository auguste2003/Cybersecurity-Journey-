lettersA = {"A","B","C","D","E","F","G"}
lettersB = {"F","G","H","I","J","K","L","M"}

union = lettersA | lettersB
print("the union ist =",union) # the oder is not garanted
intersection = lettersA & lettersB
print("The intersection =",intersection)

difference = lettersB - lettersA # everythings in letteA and not in letterB
print("The difference =",difference)