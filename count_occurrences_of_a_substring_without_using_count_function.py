main_text = input("Enter a string: ") #Ask the user for a string
substring_to_count = input("Enter a substring: ") #Ask for a substring to count

occurrence_count = 0 #Initialize a counter to 0
for index in range(len(main_text) - len(substring_to_count) + 1): #Check if the substring matches at each index by looping through the string
    if main_text[index:index+len(substring_to_count)] == substring_to_count:
        occurrence_count += 1
#Display the number of occurrences