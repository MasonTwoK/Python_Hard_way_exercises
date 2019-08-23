'''
from sys import argv #adds module argv

script, filename = argv #send arguments to variables

txt = open(filename) # returns file object

print(f"Here's your file {filename}:") # writes string in terminal
print(txt.read()) # .read returns 
txt.close()

print("Type the filename again:")
file_again = input("Type the filename again:\n> ")

txt_again = open(file_again) #this line returns file object

print(txt_again.read()) # .read() this method returns whole text
txt_again.close()
'''
#Rewrite of exercise 
from sys import argv

script, file_name = argv

txt = open(file_name)
print(f"File {file_name} contains:\n" + txt.read())
file_name.close()

ins_file = input("Enter name of file for open it:\n> ")
ins_txt = open(ins_file)
print(ins_txt.read())
ins_txt.close()