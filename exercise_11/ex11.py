print ("How old are you?", end=' ')
age = input()
print ("How tall are you?", end=' ')
height = input()
print ("How much do you weigh?", end=' ')
weight = input()

print (f"So, you're {age} old, {height} tall and {weight} heavy.")

#STUDY DRILLS
#SD-1. Go online and find out what Python’s input does.
#For prompting the manual input from user

#SD-2. Can you find other ways to use it? Try some of the samples you find.
#Of course, we can make a very simple calculator from this. Refer to SD-3 below

#SD-3. Write another “form” like this to ask some other questions.
print ("Input the first number you want to add:", end=' ')
first = int(input())
print ("Input the second number you want to add:", end=' ')
second = int(input())
total = first + second
print (f"So, {first} plus {second} is:", (total))
