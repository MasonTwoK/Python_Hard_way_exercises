#ex10.py 
'''
tabby_cat = "\tI'm tabby in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat ="""
{}\n {}\n
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
test
""".format(tabby_cat, persian_cat, backslash_cat)

print(tabby_cat)
print(persian_cat)
print(backslash_cat)

print(fat_cat)
'''
#Rewrite of exercise 
var_1 = "\tI'm tabby in."
var_2 = "I'm split\non a line."
var_3 = "I'm \\ a \\ cat."

var_4 = '''
REWrite version

I'll do a list:
\t1 Cat food
\t2 Fishies
\t3 Catnip\n\t4 Grass
'''
print("{}\n{}\n{}\n{}".format(var_1, var_2, var_3, var_4))