search_text = input("Enter a string: ") #Ask the user for a string
substring_to_find = input("Enter substring: ")#Ask for a substring to find

first_occurence_index = -1 
for index in range(len(search_text) - len(substring_to_find) + 1): #Checking for the position of the substring by looping through the string
#If there's a match, stop or break
#Display the results