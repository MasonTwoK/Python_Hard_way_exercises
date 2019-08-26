#Exercise 17 "More Files"
'''
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is \"{len(indata)}\" bytes long")

print(f"Does the output file exist? \"{exists(to_file)}\"")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
'''
'''
# Testing part which show content of 2nd file in which content were copied from 1st file.
out_file = open(to_file) 
print(f"to {to_file} contains:\n {out_file.read()}")
'''
'''
out_file.close()
in_file.close()
'''

#Rewrite of exersice 17

from sys import argv
#from os.path import exists

script, content_file, destenation_file = argv

print(f"{script} copies content from {content_file} to file {destenation_file}")
cont_obj = open(content_file)
indata = cont_obj.read()
cont_obj.close()

cont_obj = open(destenation_file, 'w')
cont_obj.write(indata)
cont_obj.close()

print(f"Coping is being completed. Check your results in file: {destenation_file}")
