text_to_align = input("Enter a string/word: ") #Ask the user for a string
desired_width = int(input("Enter total width: ")) #Ask the user for the total width

spaces_needed = max(0, desired_width - len(text_to_align)) #Calculate the spaces needed: total width - length of string
right_justified_text = " " * spaces_needed + text_to_align #Add spaces before the string
#Display the result