lowercase_text = input("Enter a string/word: ") #Ask the user for a string
uppercase_text = "" #Add a variable for uppercase text

for character in lowercase_text: #Loop through each character in the string
    if 'a' <= character <= 'z': #If the character if between "a" and "z", convert it to uppercase
        uppercase_text += chr(ord(character) - 32) 
    else: 
        uppercase_text += character #If not, add the the character as is

print("Uppercase string:", uppercase_text) #Print results