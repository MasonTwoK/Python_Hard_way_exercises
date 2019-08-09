cars = 100 #amount of cars 
space_in_a_car = 4 # amount of free seats
drivers = 30 # amount of drivers
passengers = 90 # amount of passenger seats
cars_not_driven = cars - drivers # calculates amount of free cars
cars_driven = drivers # amount of cars in which driver present
carpool_capacity = cars_driven * space_in_a_car #  amount of humans who can be in all cars
average_passengers_per_car = passengers // cars_driven #amount of passengers in driven cars

#Output after all main logic
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car , "in each car.")