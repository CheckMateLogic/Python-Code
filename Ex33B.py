#i = 0
numbers = []
Start_Value = int(input("Please provide a start value:"))
Final_Value = int(input("What value do you want me to increment too?"))
Value_to_Increment_by = int(input("What value do you want me to increment by?"))

while Start_Value < Final_Value:
    print(f"At the top i is {Start_Value}")
    numbers.append(Start_Value)

    Start_Value = Start_Value + Value_to_Increment_by
    print("Numbers now: ", numbers)
    print(f"At the bottom Start Value is {Start_Value}")


print("The numbers: ")
for num in numbers:
    print(num)
    