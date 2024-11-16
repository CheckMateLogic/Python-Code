ten_things = "1 2 3 4 5 6"

print("Wait there not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["7", "8", "9", "10", 
              "11", "12", "13", "14", 
              "15", "16", "17", "18", 
              "19", "20", "21", "22", 
              "23", "24", "25"]

print(f"{more_stuff}")
"""
while len(stuff) != 26:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)
"""
#print("Let's do some things with stuff.")
#print(stuff[1])
#print(stuff[-1]) #whoa! fancy
#print(stuff.pop())
#print(' '.join(stuff)) #what? cool!
#print('#'.join(stuff[3:5])) #super stellar!

