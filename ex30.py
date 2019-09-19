people = 30
cars = 40
trucks = 150

print("#Example 1")
if cars > people:
    print("We should take the car.")
elif cars < people:
    print("We should not take the cars.")
else: 
    print("We can't decide.")
print("#Example 2")
if trucks > cars:
    print("Maybe we could take the trucks.")
elif trucks < cars:
    print("We should not take a trucks.")
else:
    print("We still can't decide.")
print("#Example 3") #Example 3
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

print("Example 4")
if False:
   print("if True")
elif False:
    print("elif True #1")
elif False:
    print("elif True #2")
else:
    print("else")