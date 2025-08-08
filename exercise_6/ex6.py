#Defining how many types of people
types_of_people = 10
#Make variable 'x' that contain string with f-string inside of it 
x = f"There are {types_of_people} types of people."

#Defining 'binary' and 'do_not' variable
binary = "binary"
do_not = "don't"
#Call the 'binary' and 'do_not' variable inside of f-string to string
y = f"Those who know {binary} and those who {do_not}."

#print 'x' and 'y' that have been defined earlier
print (x)
print (y)

#Same as above but using f-string
print (f"I said: {x}")
print (f"I also said: '{y}'")

#Defining 'hilarious' and 'joke_evaluation'
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#Using format syntax to call the answer of 'joke_evaluation'
print (joke_evaluation.format(hilarious))

#Defining 'w' and 'e' variable
w = "This is the left side of..."
e = "a string with a right side."
#Print the string, but also using + to combine string between 'w' and 'e'
print (w + e)

#STUDY DRILLS
#SD-1. Go through this program and write a comment above each line explaining it.
#Done

#SD-2. Find all the places where a string is put inside a string. There are four places.
#In line 4 there are 1; in line 10 there are 2; in line 17 and 18 there are 2; and in line 24 there are 1

#SD-3. Are you sure there are only four places? How do you know? Maybe I like lying.
#No, there are at least 6 as i said in SD-2. Line 10 have 2, and Line 24 is actually string inside string because there are {} in the end of line 22

#SD-4. Explain why adding the two strings w and e with + makes a longer string
#You can do that because it is actually like combining the variable. So it act like 2 separate sentences and then it write the 'w' first and then 'e' second
