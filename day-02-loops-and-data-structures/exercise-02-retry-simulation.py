"""
Exercise: Retry Simulation
Name: Sumit Ojha
Day: 2
"""

# Input

attempt = 1
max_attempts = 3
opertaion_successful = False

# Approach 1

"""
while(not opertaion_successful):
    print(f"Operating on operation: {attempt}")

    if attempt == 2:
        print("Operation completed successfully")
        opertaion_successful = True

    if attempt == max_attempts:
        print("Operation failed after three attempts")
        opertaion_successful = True
    attempt+=1
"""

# Approach 2

while True:
    print(f"Operating on operation: {attempt}")

    if attempt == 2:
        opertaion_successful = True

    if attempt == max_attempts:
        print("Operation failed after three attempts")
        break 
      
    if opertaion_successful:
        print("Operation completed successfully")
        break
    
    attempt+=1
