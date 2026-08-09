"""
Exercise: Clean Numeric Values
Student: Sumit Ojha
Day: 2
"""

# Input
raw_values = [100, None, 250, "invalid", 300, None, 450]

# Calculation 
for val in raw_values:
    if isinstance(val,int):
        continue
    else:
        raw_values.remove(val)

# Output
print(raw_values)

raw_values = [100, None, 250, "invalid", 300, None, 450]

new_list = [x for x in raw_values if isinstance(x,int)]

print(new_list)