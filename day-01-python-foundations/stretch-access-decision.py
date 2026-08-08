"""
Stretch Exercise: Dataset Access Decision
Student: Sumit Ojha
Day: 1
"""

# Input
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"

# For conditional check
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_dataset = ["salary_data", "personal_data"]

# Calcualtion
if not is_active :
    print("Access denied because the user is inactive.")
elif not user_role in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_dataset:
    print("Access denied because the dataset is restricted.")