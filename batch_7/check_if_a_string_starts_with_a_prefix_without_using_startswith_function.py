full_text = input("Enter a string/word:") #Ask the user for a string
prefix_to_check = input("Enter prefix: ") #Ask the user for a prefix to check

starts_with_prefix = full_text[:len(prefix_to_check)] == prefix_to_check #Compare the first character of the string with the prefix
print("Does the string start with the prefix?", starts_with_prefix) #Display whether the string starts with the given prefix 
