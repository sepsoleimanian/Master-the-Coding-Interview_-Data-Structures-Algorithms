import time 
my_list = ["Nemo"]

def findNemo(array):
    start_time = time.perf_counter()  # Start time inside the function

    for i in range(len(array)): 
        if array[i] == "Nemo":
            print("Found Nemo! :)")
            end_time = time.perf_counter()  # End time after finding Nemo
            execution_time = end_time - start_time
            print(f"Execution time: {execution_time} seconds")
            return
    print("Nemo Not Found. :(")  
    end_time = time.perf_counter()  
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

findNemo(my_list)