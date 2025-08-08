#Defining a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print (f"You have {cheese_count} cheeses!")
    print (f"You have {boxes_of_crackers} boxes of crackers!")
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")


print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) #Calling a function that have been define with some sort of argument refering to def

print ("OR, we can use variables from our script:")
amount_of_cheese = 10 #Defining argument as variable
amount_of_crackers = 50
cheese_and_crackers (amount_of_cheese, amount_of_crackers) #calling a function using variable (that will act as argument))

print ("We can even do math inside too:")
cheese_and_crackers (10 + 20, 5 + 6) #Calling argument with integer


print ("And we can combine the two, variables and math:")
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000) #Same as above

#STUDY DRILLS
#SD-1. Go back through the script and type a comment above each line explaining in English what it does.
#Done

#SD-2. Start at the bottom and read each line backward, saying all the important characters.
#Done

#SD-3. Write at least one more function of your own design, and run it 10 different ways.
def greet_person(name, greeting):
    print(f"{greeting}, {name}!\n")
  
# 1. Direct call argument
greet_person("Alice", "Hello")

# 2. Using variables
person_name = "Bob"
greeting_text = "Hello"
greet_person(person_name, greeting_text)

# 3. With string and plus (math operator)
greet_person("Charlie", "Good" + " morning")

# 4. Using input
greet_person(input("Enter name: "), "Welcome")

# 5. Using variables and math
greet_person("User" + str(1 + 1), "Hello")

# 6. Using f-string
index = 3
greet_person(f"Person{index}", f"Hello {index}")

# 7. Using inline string operations
greet_person("david".capitalize(), "hello".upper())

# 8. Using list
names = ["Eve", "Frank", "Grace"]
greetings = ["Hi", "Hello", "Hey"]
greet_person(names[1], greetings[2])

# 9. Using function inside function
def get_name():
    return "Hannah"
greet_person(get_name(), "Hello")

# 10. Using loop
for i in range(1, 5):
    greet_person(f"Guest{i}", "Welcome")
