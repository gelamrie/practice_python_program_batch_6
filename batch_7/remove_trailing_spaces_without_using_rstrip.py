user_text = input("Enter a string with trailing spaces: ") #Ask the user to enter a string with trailing spaces and store it in a variable
trim_position = len(user_text) - 1 #Create a variable to track the last non-space character in the string

#To check for spaces, loop from the end of the string
while trim_position >= 0 and user_text[trim_position] == ' ':
    trim_position -= 1 

#Slice the string up to the last non-space character
trimmed_text = user_text[:trim_position + 1]
print("String without trailing spaces:", trimmed_text) #Print results 