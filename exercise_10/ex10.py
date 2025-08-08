tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

#STUDY DRILLS
#SD-1. Memorize all the escape sequences by putting them on flash cards.
#Okay

#SD-2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
#I think it can be used to print a long or point paragraph with ease and also print in new line without coding print in each line

#SD-3. Combine escape sequences and format strings to create a more complex format.
cat_food = "\t* Cat food\n"
fish = "\t* Fishies\n"
cat_grass = "\t* Catnip\n\t* Grass" 
fat_cat_drill = f"{cat_food} {fish} {cat_grass}"
print (f"I'll do a list:\n {fat_cat_drill}")
