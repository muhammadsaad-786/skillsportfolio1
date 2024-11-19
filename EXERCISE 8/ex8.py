# Making a list of strings with all names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Defining search function
def search_name(names_list, search_term):
    for name in names_list:
        if name == search_term:
            return f"{search_term} is found in the list. What would you like to know?"
    return f"Unfortunately {search_term} was not found in the list. Please ensure the spelling are correct :)"

# Making the player input the name to be searched
search_term = input("Hey there! Kindly provide with a name to search for. ")

# Using the search function
result = search_name(names, search_term)

# Printing the program 
print(result)