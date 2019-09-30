
string = "Apples Oranges Crowns Telephone Light Sugar"
array  = string.split(' ')

print("Wait there are not 10 things in that list. Let's fix that.")

new_elements = ["Corn", "Banana", "Girl", "Boy"]

while len(array) != 10:
    next_element = new_elements.pop()
    array.append(next_element)
    print(f"Adding: {next_element} \nThere are {len(array)} items now.")

print("There we go: {}".format(array))

print("Let's do some things with stuff.")
print(array[1])
print(array[-1])
print(array.pop())
print(' '.join(array))
print('#'.join(array[3:5]))