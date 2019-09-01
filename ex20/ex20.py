'''
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file, 'r')

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = 2
print_a_line(current_line, current_file)

current_line = 3
print_a_line(current_line, current_file)
'''

#Rewrite of exercise 20

from sys import argv

script, name_of_file = argv
file_obj = open(name_of_file)

def file_returner(file):
    print("Printing the whole file...\n")
    print(file.read())
    file.seek(0) # rewindes file to the start
def rewinder_line_returner(file, number_of_lines):
    for line_number in range(0, number_of_lines):
        print(line_number + 1, file.readline())

file_returner(file_obj)
print()
rewinder_line_returner(file_obj, 3)