# Exercise 19 Functions and Variables
'''
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20 , 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100 , amount_of_crackers + 1000)
'''

#Rewrite of exercise
print("Rewrite of Exercise 19")
def function(num1, num2):
    print(f"You have {num1} cheeses!")
    print(f"You have {num2} boxes of crackers!")
    print("Man that's enought for a party!")
    print("Get a blanket.")

print("Example 1. Direct numbers")
function(20, 30)

print("Example 2. Out script call")
var1 = 10
var2 = 50 
function(var1, var2)

print("Example 3. Math inside parameters")
function(20 + 10, 1 + 10)

print("Example 4. Variables + math")
function(var1 + 100, var2 + 1000)
