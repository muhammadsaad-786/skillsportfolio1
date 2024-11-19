# Defining the function
def check_odd_even(number):
    if number % 2 == 0:    # If number is divided by 2 and ends up getting 0, it is even
        return "The following number is even!"
    else:    # If number is divided by 2 but the answer doesnt end up getting 0, it is odd
        return "The given number is odd!"   
    
def central():     # Defining main function
    number = int(input("Enter any number you like: "))    # Asking the player to input any value
    result = check_odd_even(number)
    print(result)      # Printing the final result

if __name__ == "__main__":
 central()