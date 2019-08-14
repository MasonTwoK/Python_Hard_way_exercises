'''
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So you're {age} old, {height} tall and {weight} heavy.")
'''

#Study drill
#Program calculates BMI
age = int(input("How old are you? "))
height = int(input("How tall are you? "))
weight = int(input("How much do you weight? "))
bmi = weight / ( (height/100) ** 2 )

print(f"So you're {age} old, {height} tall and you weight {weight}")
print(f"BMI is equal {round(bmi, 2)}")
