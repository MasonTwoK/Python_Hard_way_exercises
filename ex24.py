'''
print("Let's practice everything.")
print('You\'d need to know\'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none. 
"""

print("-------------")
print(poem)
print("-------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with an f'' string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
'''

#Rewrite of exercise 24

print("Let's practice everything.")
print('You\' need to know\'bout escapes with \\ that do: ')
print('\nnewlines and \ttabs.')

poem = """
\tThe lovely world
with logic so firmly planted\ncannot discern
the needs of love
nor comprehend passion form intuition
and requires an explanation
\n\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 + 1 - 2 + 4
print(f"This should be five: {five}")

def math_function(start_point):
    beans = start_point * 500
    jars = start_point / 2
    crates = start_point / 200
    return beans, jars, crates

num = 10000
print("With starting point of: {}".format(num))

ans1, ans2, ans3 = math_function(num)

print(f"We'd have {ans1} beans, {ans2} jars, and {ans3} crates.")
print("We can also do that this wway:")

answers = math_function(1000)
print("We'd have {} beans, {} jars, and {} crates.".format(*answers))