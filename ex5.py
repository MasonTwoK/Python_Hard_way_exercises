name = 'Zed A. Show'
age = 35 
height = 74 * 2.54 # inches
weight = 180 * 0.4 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilos heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = round(age + height + weight)
print(f"If I add {age}, {height}, and {weight} I get {total}.")