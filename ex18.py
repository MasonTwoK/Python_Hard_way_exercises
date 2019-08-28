# Names, Variables, Code, Functions
'''
# this one is like your scripts with argv
def print_two(*argv):
    arg1, arg2 = argv
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin' .")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
'''

#Rewrite of exercise
def func_with_group_of_param (*args):
    arg1, arg2, arg3 = args
    print("{} {} {}".format(arg1, arg2, arg3))

def func_with_two_param(arg1 ,arg2):
    print (arg1 , arg2)

def func_with_one_param(arg1):
    print(arg1)

def func_with_out_param():
    print("function does not contain parameters")

func_with_group_of_param(1,2,3)
func_with_two_param("Parameter one" , "Parameter two")
func_with_one_param("Only one parameter")
func_with_out_param()