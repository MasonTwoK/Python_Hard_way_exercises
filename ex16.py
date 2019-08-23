'''
close - Closes file.
read - Reads content of file
readline - Reads only one line of text
truncate - Empties the file.
write('stuff') - Writes "stuff" to file
seek(0) - Move the read/write location to beginning of the file. 
'''
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don;t want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate() #Why do we use truncate() 

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(
line1 + "\n" + line2 + "\n" + line3 + "\n"
)
target.close()


print ("Here is your lines")
target = open(filename)
print(target.read())
print("And finally, we close it.")
target.close()