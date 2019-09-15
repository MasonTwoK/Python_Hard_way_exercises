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

script, txt_file = sys.argv

def main(ob_f, encoding, er):
    string_printer(ob_f, encoding, er)
    return main(ob_f, encode, error)

def string_printer(ob, encode, err):
    single_string = ob.readline()
    raw_byte = single_string.encode(encoding=encode, errors=err)
    cooked_byte = single_string.decode(encode, errors=err)

    print(cooked_byte, "<===>", raw_byte)


obj_file = open(txt_file, encoding="utf-8")
main(obj_file, "utf-8", "strict")
