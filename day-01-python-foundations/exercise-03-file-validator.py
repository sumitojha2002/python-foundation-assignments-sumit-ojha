"""
Exercise: File Validator
Student: Sumit Ojha
Day: 1 
"""
# Tuple 
accepted_file_type = (".csv",".json", ".parquet",".xlsm")

while(1):
    # User Input
    file = input("Enter the file name and \"exit\" to exit loop: ")

    # Remove white spaces and lower case the string.
    file_name = file.strip().lower()

    # Condition checking
    if file_name.endswith(accepted_file_type):
        print(f"File name: {file_name}\n")
    elif file_name != "exit":
        print(f"This file is not accepted.\n")

    file_name == "exit"  and exit()