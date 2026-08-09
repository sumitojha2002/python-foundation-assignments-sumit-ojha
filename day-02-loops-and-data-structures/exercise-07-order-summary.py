"""
Exercise: Nested Order Summary
Student: Sumit Ojha
Day: 2
"""

# Input
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

#Calculation

order_customer = {
    order:{customer:name 
         for customer,name in values.items() 
             if customer == "customer"
            }
        for order,values in orders.items()
                  }

completed_order = {
    order_id:odrs 
    for order_id,odrs in orders.items() 
    if odrs["status"] == "Completed" 
}

count_pending ={
    order_id for order_id,odrs in orders.items() if odrs["status"] == "Pending"
}

orders["ORD-004"] = {"customer":"Sumit","amount":1400,"status":"Completed"}

# Output
print(f"\nOrder ID and cutomer: {order_customer}\n")
print(f"\nCompleted order set: {completed_order}\n")
print(f"\nCount of pending orders: {len(count_pending)}\n")
print(f"\nAfter adding new data: {orders}\n")

