def main():
    #Create a dictionary to store information
    user_details = {}
    
    #Get user input for name, hometown and age
    user_details['Name'] = input(" Enter your name (First and Last): ") 
    user_details['Hometown'] = input(" Enter your Hometown:")
    
    # Loop until a valid age is provided
    while True:
        age_insert = input("Enter your age: ")
        if age_insert.isdigit(): # Check if the input is a digit
            user_details['Age'] = int(age_insert) #Turn into integer form
            break # End the oop if transforming is accomplished
        else:
            print("Please enter a valid digit for your age")
            
    # Print the values stored in the dictionary
    print("\n The Data")
    print("\nYOur information:")
    print(f"Name: {user_details['Name']}\nHometown: {user_details['Hometown']}\nAge: {user_details['Age']}")
    
if __name__ == "__main__":
    main()