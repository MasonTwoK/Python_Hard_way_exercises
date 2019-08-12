'''
print("Mary had a little lamb.")

#string call function .format() which takes string 'snow' and paste it in to {} place
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.") #Casual call of print() functions which outputs string "And everywhere that Mary went." 
print("." *10) #what'd that do? <-- this line multiplicates character '.' 10 times 
#Group of values which contain one character
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. try removing it to see what happens  <-- Syntax error appears
print(end1 + end2 + end3 + end4 + end5 + end6,  end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
'''
#Rewrite of exercise
print("Mary had a little lamb.")
print("Its fleece was {}".format("white as snow"))
print("And everywhere that Mary went.")
print('.' * 10)

char0 = 'E'
char1 = 'l'
char2 = 'i'
char3 = 'z'
char4 = 'a'
char5 = 'b'
char6 = 'e'
char7 = 't'
char8 = 'h'
char9 = "3rd"

print(char0 + char1 + char2 + char3 + char4, end ='')
print (char5 + char6 + char7 + char8 + ' ' + char9)