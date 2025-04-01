original_text = input("Enter a string/word: ") #Ask the user for a string
suffix_to_remove = input("Enter suffix to remove: ") #Ask the user for a suffix to remove

#Check if the string end with the suffix
if original_text.endswith(suffix_to_remove):
    modified_text = original_text[:-len(suffix_to_remove)] #If yes, remove the suffix by slicing
else: #If no, keep the strings unchanged
    modified_text = original_text
    
#Display the results 