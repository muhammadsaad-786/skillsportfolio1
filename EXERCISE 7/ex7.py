# Loop 1: Counting values from 0 to 50 in increments of 1  

s = 0   # setting initial value
for _ in range(51):  # Loop will be running 51 times
    print(s)
    s += 1   # Incrementing by 1
    
# Loop 2: Counting down from 50 to in decrements of 1

a = 50   # setting the initial value
for _ in range(51):   # Loop will run for 51 times
    print(a)
    a -= 1     # Decrementing by 1
    if a < 0:     # When required value is achieved, stop the loop
        break
    
# Loop 3: Counting from 30 to 50 in increments of 1

b = 30     # setting the initial value
for _ in range(21):      # Loop will run for 21 times (50-30+1)
    print(b)
    b += 1      # Incrementing by 1

# Loop 4: Counting down from 50 to 10 in decrements of 2

c = 50    # Setting the initial value
for _ in range(21):    # Loop will run for 21 times (50-10/2+1)
    print(c)
    c -= 2     # Decrementing by 2
    if c < 10:    # When required value is obtained, stop the loop
        break
    
# Loop 5: Counting from 100 to 200 in increments of 5

d = 100     # Setting the initial value
for _ in range(21):     # Loop will run for 21 times (200-100/5+1)
    print(d)
    d += 5     # Incrementing by 5