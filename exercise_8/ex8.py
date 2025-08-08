formatter = "{} {} {} {}" #Defining some sort of f-string. We must enter FOUR argument to fulfill this variable. If not, then it will cause an error when you run it

print (formatter.format(1, 2, 3, 4)) #Like this, 4 argument
print (formatter.format("one", "two", "three", "four")) 
print (formatter.format(True, False, False, True))
print (formatter.format(formatter, formatter, formatter, formatter)) #It will do formatter 4 times
print (formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) 
#Even its in different line, but it is to fulfill the variable so it will be in one single line. We can see the identation because without it, then it will broke the code

#STUDY DRILLS
#Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise. In other words, repeat the Study Drills from Exercise 7.
#Done
