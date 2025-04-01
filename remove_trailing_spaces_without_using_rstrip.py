user_text = input("Enter a string with trailing spaces: ") #Ask the user to enter a string with trailing spaces and store it in a variable
trim_position = len(user_text) - 1 #Create a variable to track the last non-space character in the string

#To check for spaces, loop from the end of the string
#Slice the string up to the last non-space character
#Print results 