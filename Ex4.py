# creates variable cars as an integer. Integer assigned 100
cars = 100

#creates variable space_in_a_car as a float. Float assigned 4.0
space_in_a_car=4

#creates variable drivers as an integer. Integer assigned 30
drivers = 30

#creates variable passenger as an integer. Integer assigned 90
passengers = 90

#creates variable cars_not_driven by subtracting cars minus drivers. The result is 100-30 = 70.00
cars_not_driven = cars - drivers

#creates variable cars_driven as an integer. 
# Integer equal to drivers.
#
#???Why would someone set a variable equal to another variable???

# It appears that when assigning a variable another variable it defaults the new variable to a float. 
# ??? Why??? The programmer does not know.
cars_driven = drivers

#creates variable carpool_capacity  which is equal
#two variables multiplied two variables cars_driven(30)* space_in_a_car(4.0)
#   !!!Careful!!!
#   This variable is multiplying an integer and a float. The resulting value is ASSUMED Float
#   !!!Careful!!!
carpool_capacity = cars_driven * space_in_a_car

#creates variable average_passenger_per_car.
# Variable is equal to passengers(90)/cars_driven(30)
#   !!!Careful!!!
#  When dividing numbers sometimes the value is irational(a float) 
# does this change the Integer to a float or does it truncate/round to keep it an integer
#  ??? The answer is unknown??? Programmer
#   !!!Careful!!!
average_passenger_per_car = passengers/cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")

