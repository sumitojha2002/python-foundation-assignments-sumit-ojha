"""
Exercise 5: Pipeline Health Status
"""
# Input
data = {
    "data_1":{
        "rows_loaded" : 9800,
        "rows_failed" : 200,
        "runtime_minutes" : 18
    },
    "data_2":{
        "rows_loaded" : 9500,
        "rows_failed" : 500,
        "runtime_minutes" : 15
    },
    "data_3":{
        "rows_loaded" : 9900,
        "rows_failed" : 100,
        "runtime_minutes" : 30
    }
}

# Loop
for data_key, data_val in data.items():
    runtime = data_val["runtime_minutes"]   
    

    # Calcualtion
    total_data = data[data_key]["rows_failed"]+data[data_key]["rows_loaded"]
    failure_rate = data[data_key]["rows_failed"] / total_data * 100


    # Condition given 
    # Healthy: Failure rate is at most 2% and runtime is at most 20 minutes.
    # Warning: Failure rate is more than 2% but at most 5%.
    # Critical: Failure rate is more than 5%.
    # Display the failure rate and final pipeline status.

    # if we follow as said then we would get
    
    # if failure_rate <= 2.0 and runtime <= 20:
    #    status= "Healthy"
    # elif failure_rate >2.0 and failure_rate <= 5%:
    #   status= "Warning"
    # else:
    #   status = "Healthy"
    
    # Calculation using diff approach
    if failure_rate > 5.0:
        status = "Critical"
    elif failure_rate > 2.0 or runtime > 20:
        status = "Warning"
    else:
        status = "Healthy"

    # Output
    print(f"Data: {data_key}\n")
    print(f"rows_loaded: {data[data_key]["rows_loaded"]}")
    print(f"rows_failed: {data[data_key]["rows_failed"]}")
    print(f"runtime_minutes: {runtime}")
    print(f"failure_rate: {failure_rate:.2f} %\n")
    print(f"Status: {status}\n\n")

    # so the main question is to consider the 3rd option "healthy"
    # as making the logic in another way we get different result resulting 3rd 
    # data as "Warning" and 1st logic "Critical" as runtime was being checked first 

print("--- Final Case Analysis ---")
print("Answer: No, the final case should NOT be classified as healthy.")
print("Reason: Even though its failure rate is low (1.00%), it breaches")
print("        the maximum allowed runtime limit of 20 minutes.")
print("        Therefore, it is correctly downgraded to a 'Warning'.")
    
