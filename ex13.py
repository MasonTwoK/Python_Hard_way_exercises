# Exercise 13 Parameters, Unpacking, Variables
'''
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your fird variable is:", third)
'''

from sys import argv

script_name, user_name = argv


user_surename = input("Enter your Surename: ")
print("Hi, " + user_name +" "+ user_surename)
