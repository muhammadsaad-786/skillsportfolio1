def central():
    # Creating a dictionary for Countries and thweir Capitals
    country_names = {  
    "Pakistan": "Islamabad",  
    "China": "Beijing",  
    "Germany": "Berlin",  
    "Japan": "Tokyo",  
    "Brazil": "Brasilia",  
    "India": "New Delhi",  
    "UAE": "Abu Dhabi",  
    "Saudi Arabia": "Riyadh",  
    "Afghanistan": "Kabul",  
    "Philippines": "Manila", 
  
    }
    
    # Setting the Right Count from 0
    right_count = 0
    
    # Initializing the for loop for the countries 
    for country, capital in country_names.items():
        
        # Ask the player about the question
        player_reply = input(f"What is the Capital of {country}? ").strip()
        
        #Inspect whether the answer of player is correct or incorrect
        if player_reply.lower() == capital.lower():
            print("Yess, You're correct!")
            #Increase the value by 1 for each correct reply
            right_count += 1 #in case of wrong answer, reply them
        else:
            print(f"Nuh-uh, The right answer for this was {capital}. ")
             
    # Print the final result
    print(f"\nYou got {right_count} out of {len(country_names)} Right. Hurray!")

central()