input_text = input("Enter a string/word: ") #Ask user for a string
all_lowercase = True #Assume that the string is all lowercase

#Loop through each character
for character in input_text:
    if 'A' <= character <= 'Z': #If there is any detected character between 'A' and 'Z', change the assumption to False and break
        all_lowercase = False
        break 
    
print("Is the string all lowercase?", all_lowercase)#Print results