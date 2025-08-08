#Import library
from sys import argv

#Defining argument using argv
script, filename = argv

#Variable to open txt file
txt = open(filename)
#Printing the file name and execute read txt command
print (f"Here's your file {filename}:")
print (txt.read())
#Same as above, repeated
print ("Type the filename again:")
file_again = input ("> ")
#Same as above
txt_again = open(file_again)
#Read the txt file
print (txt_again.read())

#STUDY DRILLS
#SD-1. Above each line, comment out in English what that line does.
#Done

#SD-2. If you are not sure, ask someone for help or search online. Many times searching for “python3.6 THING” will find answers to what that THING does in Python. Try searching for “python3.6 open.”
#Okay
