search_text = input("Enter a string: ") #Ask the user for a string
substring_to_find = input("Enter substring: ")#Ask for a substring to find

first_occurence_index = -1 
for index in range(len(search_text) - len(substring_to_find) + 1): #Checking for the position of the substring by looping through the string
    if search_text[index:index+len(substring_to_find)] == substring_to_find: 
       first_occurrence_index = index
       break #If there's a match, stop or break

print("First occurrence index:", first_occurrence_index if first_occurrence_index != -1 else "Not found") #Display the results