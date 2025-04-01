string = input("Enter a string/word: ") #Ask the user for a string
required_width = int(input("Enter total width: "))#Ask for the required total width

zeros_needed = max(0, required_width - len(string)) #Compute the number of zeros needed: required width - length of string
zero_filled_string = "0" * zeros_needed + string #Add zeros before the string
#Print results
