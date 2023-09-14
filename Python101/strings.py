# strings in general are sequence of characgters enclosedd within a pair quotes (single or double or triple)
fName = 'Srikanth'
lName = "Vadapalli"
desc = '''I am a graduate in technology.
I am working for and IT firm with a  12+ years total experience.
Currently exploring options to establish my career and earn huge amount of salerie.
Also willing to do secondary job to have more earnings! '''

# String methods
print("Length of the {0} is {1}".format(fName, len(fName)))
print(f"Upper case of {lName} is {lName.upper()}")
print(f"Lower case of {fName} is {fName.lower()}")
print("Capitalized {0} is {1}".format((fName+lName).casefold(), (fName+lName).capitalize()))
print(desc[:]) # It prints all characters in the string
print(desc[0:10]) # It prints first 10 characters in the string
print(desc[::2]) # It prints the string with a spacing of two characters
print(desc[::-1]) # It prints the string in reverse order
print("     What a power in string methods       ".strip()) # It prints the string after removing the leading & ending spaces
print(desc.split()) # It will split the string into list of elements
