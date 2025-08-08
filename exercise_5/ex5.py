name = "Zed A. Shaw"
age = 35 
height = 74 #inches
weight = 180 #lbs
height_cm = height * 2.54 #inches to cm
weight_kg = weight * 0.453592 #pounds to kg
eyes = "Blue"
teeth = "White"
hair = "Brown"

print (f"Let's talk about {name}.")
print (f"He's {height_cm} cm tall.")
print (f"He's {weight_kg} kg heavy.")
print ("Actually that's not too heavy.")
print (f"He's got {eyes} eyes and {hair} hair.")
print (f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height_cm + weight_kg
print (f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")

#STUDY DRILLS
#SD-1. Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.
#Done

#SD-2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.
#In line 5 and 6. I also change the variable in print
