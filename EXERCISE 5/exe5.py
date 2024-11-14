# Making a dictionary to track month names to number of days  
months_days = {  
  "January": 31,  
  "February": 28,  
  "March": 31,  
  "April": 30,  
  "May": 31,  
  "June": 30,  
  "July": 31,  
  "August": 31,  
  "September": 30,  
  "October": 31,  
  "November": 30,  
  "December": 31  
}  
  
# Ask the player to fill in the name of the month  
month = input("Heyyy!! Enter the name of the month (e.g. January, February, etc.): ")  
  
# Verify if the player entered correct input  
if month in months_days:  
  # Verify if the month is feb & whether it's a leap year or no 
  if month == "February":  
    is_leap_year = input("Ouuu! Is it a leap Year? (Yes/No)")  
    if is_leap_year.lower() == "yes":  
        months_days["February"] = 29  
    else:  
        months_days["February"] = 28  

  # Print the num of days in corresponding month  
  print(f"There are {months_days[month]} days in {month}.")  
else:  
  print("Nuh-uh, wrong month name dude.")