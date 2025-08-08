#Variable for cars, specify that there are 100 cars
cars = 100
#Variable for space in a car, specify that there are 4 seat for each car
space_in_a_car = 4.0
#Variable for drivers, specify that there are 30 drivers
drivers = 30
#Variable for car passenger, specify that there are 90 passengers
passengers = 90
#Variable for undriven car, this is a math operator
cars_not_driven = cars - drivers
#Variable for car that been used, this is a math operator
cars_driven = drivers
#Variable for car pool capacity, this is a math operator
carpool_capacity = cars_driven * space_in_a_car
#Variable for average passenger per car, this is a math operator
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

#Line 1 to 8 is just variable, the name can be different but don't forget, if you change the variable names then you must adjust the rest

#Refer to book, there are some error. Explain this error in your own words. Make sure you use line numbers and explain why
#NameError: name 'car_pool_capacity' is not defined
#This is because 'car_pool_capacity is not yet defined as variable, instead use 'carpool_capacity'

#SD-1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
#If to calculate something that integer (like space in a car) then it is not necessary. .0 is to specify that the number is floating point

#SD-2. Remember that 4.0 is a floating point number. It’s just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
#Okay

#SD-3. Write comments above each of the variable assignments.
#Done

#SD-44. Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
#Okay

#SD-5. Remember that _ is an underscore character.
#Okay

#SD-6. Try running python3.6 from the Terminal as a calculator like you did before, and use variable names to do your calculations. Popular variable names include i, x, and j
#Done, the answer as follow
#There are 100 cars available.
#There are only 30 drivers available.
#There will be 70 empty cars today.
#We can transport 120 people today.
#We have 90 to carpool today.
#We need to put about 3 in each car.
