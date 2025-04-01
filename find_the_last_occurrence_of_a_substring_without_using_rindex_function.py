search_text = input("Enter a string: ") #Ask the user for a string
substring_to_find = input("Enter substring to find from the end: ") #Ask for a substring to find from the end

last_occurrence_index = -1
#Check if the substring matches at each index by looping through the string backwards
#Stop if there's a match
#Display the index