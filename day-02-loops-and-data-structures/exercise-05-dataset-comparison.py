"""
Exercise: 5
Student: Sumit Ojha
Day: 2 
"""

# Input
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# Calcualtion
unique_data = dataset_a ^ dataset_b
union =  dataset_a & dataset_b
onlyin_dataset_a = dataset_a - dataset_b
onlyin_dataset_b = dataset_b - dataset_a

# Output
print(f"All unique dataset names: {unique_data}")
print(f"Datasets found in both groups: {union}")
print(f"Datasets only in dataset_a: {onlyin_dataset_a}")
print(f"Datasets only in dataset_b: {onlyin_dataset_b}")