
def study_drill_func(var1, var2):    
    
    i = 0
    numbers = []

    for i in range(i,var1,var2):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: i", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

study_drill_func(7, 1)