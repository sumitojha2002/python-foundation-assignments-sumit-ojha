"""
Exercise: Sales Summary
Student: Sumit Ojha
Day: 1
"""

# Input Values
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Calculations
gross_sales = unit_price * quantity_sold
discount = gross_sales * discount_percentage
final_sales = gross_sales - discount

# Output
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount:.2f}")
print(f"Final sales: NRP {final_sales:.2f}")

