"""
Exercise : Batch Processor
Student: Sumit Ojha
Day: 2
"""
# Loop
for batch_number in range(10):

    # if(batch_number == 0):
    #     continue

    # Condition
    if(batch_number % 3 == 0):
        print("Checkpoint reached")
    else:
        print(f"Processing batch {batch_number}")