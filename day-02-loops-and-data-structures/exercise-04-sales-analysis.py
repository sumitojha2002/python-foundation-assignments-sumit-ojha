'''
Exercise: Sales Analysis
Student: Sumit Ojha
Day: 2
'''

# Input
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# Calcualtion
# Sorting ascending order
monthly_sales.sort()
# Values > 100000
list_greater_then_100000 = [sales for sales in monthly_sales if sales > 100000]
# Adding 13% vat
vat_added = [sales +0.14*sales for sales in monthly_sales]
total_sum = sum(monthly_sales)
avg_sales_amount = total_sum/len(monthly_sales)

# Output
print(f"Ascending order: {monthly_sales}")
print(f"Amount greater then 100000: {list_greater_then_100000}")
print(f"VAT added List: {vat_added}")
print(f"Total sum: NRP {total_sum:.2f}")
print(f"Avg sales amount: NPR {avg_sales_amount:.2f}")