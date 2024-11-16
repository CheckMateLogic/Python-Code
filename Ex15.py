#from sys import argv

#script, filename = argv
#Opens file 
#txt = open(filename)

#print(f"Here's your file {filename}:")
#prints everything inside the file.
#print(txt.read())

#print("Type the filename again:")

file_again = input("Please insert the file you wish to read:")

txt_again = open(file_again)

print(txt_again.read())
