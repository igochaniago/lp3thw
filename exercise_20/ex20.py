#Import library
from sys import argv
#Define the argv
script, input_file = argv
#Define print_all function
def print_all(f):
    print (f.read())
#Define rewind function
def rewind(f):
    f.seek(0)
#Define print_a_line function
def print_a_line(line_count, f):
    print (line_count, f.readline())
#Variable to open the file from argument input
current_file = open(input_file)

print ("First, let's print the whole file:\n")
#Print the current_file content
print_all(current_file)

print ("Now, let's rewind, kind of like a tape.")
#Back to start of the file
rewind(current_file)

print ("Let's print three lines:")
#Print first line
current_line = 1
print_a_line(current_line, current_file)
#Print second line -> current_line=1 so 1+1=2
current_line += 1
print_a_line(current_line, current_file)
#Print third line -> current_line=2 so 2+1=3
current_line += 1
print_a_line(current_line, current_file)

#STUDY DRILLS
#SD-1. Write an English comment for each line to understand what that line does.
#Done

#SD-2. Each time print_a_line is run, you are passing in a variable, current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.
#Done, in comment line 27, 29, 32

#SD-3. Find each place a function is used, and check its def to make sure that you are giving it the right arguments.
#Okay

#SD-4. Research online what the seek function for file does. Try pydoc file, and see if you can figure it out from there. Then try pydoc file.seek to see what seek does.
#Okay

#SD-5. Research the shorthand notation +=, and rewrite the script to use += instead.
#Okay, we used it in Line 30 and 33
