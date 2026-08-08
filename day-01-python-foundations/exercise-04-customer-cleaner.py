"""
Exercise: Customer Record Cleaner
Student: Sumit Ojha
Day: 1
"""

# Input
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

name = raw_name.strip().lower()

# name is converted into list
name = name.split(" ")

# Calculation
# Capitalize the first letter of the str
first_name = name[0].capitalize()
second_name = name[1].capitalize()

# name
name = first_name +" "+ second_name 
# city
city = raw_city.strip().lower().capitalize()
# age
age = int(raw_age)
# email
email = raw_email.strip().lower()
# status
status = "Adult" if age >= 18 else "Minor" 

# Output
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")