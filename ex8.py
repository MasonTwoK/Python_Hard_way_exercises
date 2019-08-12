#ex8 Printing, Printing
'''
formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
'''
#Repeat of exercise 
string  = "{} {} {} {}"

print(string.format(1,2,3,4)) # need to try to add more args then in actual string
print(string.format(string, string, string, string))
print(string.format("You", "the", "sun" , "flower"))
print(string.format("Next is", "boolean type:", True, False))