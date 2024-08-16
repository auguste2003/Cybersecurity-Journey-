"""
Creating files in python
"""
file = open('./myfile.txt', 'w')
file.write('Hello World\n')
file.write("id,name,email\n")
file.write("1,Djamila,djamila@gmail.com\n")
file.close()