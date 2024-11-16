# Creates a variable as a string?
# Variable is the name of the author of the book "Learn Python 3 the hard way"
my_name = 'Zed A. Shaw' 

#creates variable my_age assignes it integer of 35 
my_age = 35

#creates variable my_height assignes variable integer 74
# Units are in inches 
my_height = 74 #inches

#creates variable my_weight assignes it integer 180
# Units are in lbs
my_weight = 180 #lbs

#creates variable my_eyes, assigns varialbe a string, String name is Blue
my_eyes = 'Blue'

#creates variable my_teeth, assigns it a string, string name White
my_teeth = 'White'

#creates variable my_hair and assigns it a string, string name Brown
my_hair = 'Brown'

# ??? Unknown ??? 
# I don't know why there is an f inside print command. Why is it there and what is it doing?
# ??? Unknown ???

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usally {my_teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

