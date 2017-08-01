# ex15.py Reading files

# use argv to read a file
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

# use input() to read a file
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
