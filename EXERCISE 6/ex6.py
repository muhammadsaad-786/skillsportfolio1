# Defining the correct passcode  
pass_code = "197100"  
  
# Initializing the num of attempts  
attempts = 0  
  
# Using a while loop to repeatedly ask the player for the passcode  
while attempts < 5:  
  # Ask the user for the password  
  player_input = input("Kindly enter the passcode: ") 
  
  # Verify if the password is correct  
  if player_input == pass_code:  
    # Output an appropriate message when the correct password is entered  
    print("Authorization Complete, Welcome Back!")  
    break  
  else:  
    # Incrementing the num of attempts  
    attempts += 1  
  
    # Informing the player of the remaining attempts  
    remaining_attempts = 5 - attempts  
    print(f"Incorrect Passcode! You have {remaining_attempts} attempts remaining. Please enter the correct passcode")  
  
# If the maximum number of attempts is reached, inform the user that the authorities have been alerted  
if attempts == 5:  
  print("Max number of attempts reached! Authorities have been alerted :/")