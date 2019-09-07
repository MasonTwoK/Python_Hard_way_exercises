'''
import sys
#Page 115
script, input_encoding, error =  sys.argv #Why do we need use name of module sys.

def main(language_file, encoding, errors):
    line = language_file.readline() #Takes line from object

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

#Function which prints line
def print_line(line, encoding, errors):
    next_lang = line.strip() #Q: What .strip() does A: https://www.programiz.com/python-programming/methods/string/strip
    raw_bytes = next_lang.encode(encoding, errors = errors) # .encode()
    cooked_string = raw_bytes.decode(encoding, errors = errors) # .decode()

    print(raw_bytes, "<===>", cooked_string)

#1. converting lang..txt to lang.. object
languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)
'''


import sys

script, lang_file = sys.argv

def main(file_ob, form, error):
    file_line = file_ob.readline()

    if file_line:
        line_printer(file_line, lform = form, lerror = error)    
        return main(file_ob, form, error)

def line_printer(line, lform, lerror):
    final_line = line.strip()
    raw_byte = final_line.encode(lform, lerror)
    cooked_byte = raw_byte.decode(lform, lerror)
    
    print(f"{raw_byte} <===> {cooked_byte}")


languges = open(lang_file, encoding = "utf-8")
main(languges, "utf-8", "strict")

