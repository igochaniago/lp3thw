from sys import argv

script, username, password = argv
prompt = '>>> '

print (f"Hi {username}, I'm the {script} script.")
print ("I'd like to ask you a few questions.")
print (f"Do you like me {username}?")
likes = input(prompt)

print (f"Where do you live {username}?")
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print (f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

#STUDY DRILLS
#SD-1. Find out what the games Zork and Adventure were. Try to find copies and play them.
#Okay, consider it done

#SD-2. Change the prompt variable to something else entirely.
#Consider it done in line 4

#SD-3. Add another argument and use it in your script, the same way you did in the previous exercise with first, second = ARGV.
#Done in line 3 i add one argument -> password

#SD-4. Make sure you understand how I combined a """ style multiline string with the {} format activator as the last print.
#Okay
