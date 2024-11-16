#Creates a variable, integer, assigns it 10
types_of_people = 10
#Creates a string x, Assigns string "There are 10 types of people."
x = f"There are {types_of_people} types of people."

#creates string binary, assigns it binary
binary = "binary"
#creates string do_not, assigns it don't
do_not = "don't"
#creates string y, assigns it "Those who know binary and those who don't"
y = f"Those who know {binary} and those who {do_not}"

#prints x and y
#There are 10 types of people.
#Those who know 10 and those who don't
print(x)
print(y)

#Creates a string inside print.
#I said: There are 10 types of people
print(f"I said: {x}")
#I also said: Those who know binary and those who do_not
print(f"I also said: '{y}'")

#Creates a variable/string assigns it False
hilarious = False

#creates string, Assigns it "Isn't that joke so funny"
joke_evaluation = "Isn't that joke so funny?! {}"

#prints "False"
print(joke_evaluation.format(hilarious))
#Creates string w, assigns it "This is the left side of..."
w = "This is the left side of..."
#creates a string e, assigns it "a string with a right side."
e = "a string with a right side."

#prints both w and e in sequence
# This is the left side of... a string with a right side.
print(w+e)

