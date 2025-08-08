from sys import argv

script, first, second, third = argv #Must include 4 statement after type "python"
#example: python ex13.py this is it
#ex13.py = script arg
#this = first arg
#is = second arg
#it = third arg
print ("Before continue, how many arguments that you type:", end=' ')
arg_count = input()
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
print (f"I can see this because i input: {arg_count} arguments")

#STUDY DRILLS
#SD-1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
#The error -> Traceback (most recent call last): File "<stdin>", line 1, in <module> ValueError: not enough values to unpack (expected 4, got 1)
#We cannot run it simply because we use argv library and we define it having 4 arguments. So less than 4 argument then it wont open

#SD-2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
#Done

#SD-3. Combine input with argv to make a script that gets more input from a user. Don’t overthink it. Just use argv to get something, and input to get something else from the user.
#Done, in line 9 and 10

#SD-4. Remember that modules give you features. Modules. Modules. Remember this because we’ll need it later.
#Okay
