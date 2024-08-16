"""
Working with Files
"""
import os.path  # bibliothe to check if there is a path

file = open('./myfile.txt', 'r')
#print(file.read())
# for line in file:
#   print(line)
print(file.readlines())
file.close()

# Alternative to the function close()

filename = './myfile.txt'

if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())

else:
    print(f'File {filename} does not exists')
