types_of_people = 10 # assaing 10 to variable types_of_people
x = f"There are {types_of_people} types of people." # created variable x with f-string  

binary = "binary" # created simple variable
do_not = "don't" # created simple variable
#string inside string 1,2
y = f"Those who know {binary} and those who {do_not}." # varible with f-string
#printing empty line. Next line is output of x variable. After that line output of y variable.   
print() 
print(x)
print(y)
# Next two lines printing strings with text and with string variable x and variable y in next line  
print(f"I said: {x}") #string inside string 3
print(f"I also said: '{y}' ") #string inside string 4
#Variable gets boolean type value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" #String with place holder

print(joke_evaluation.format(hilarious)) #print function in which .format function adds hilarious variable

w = "This is the left side of..."
e = "a string with right side."
# print function contatenate two variables with + operator
print(w + e)