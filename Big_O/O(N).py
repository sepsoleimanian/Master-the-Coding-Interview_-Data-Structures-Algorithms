import time

nemo = ["nemo"]
names = ["sep"] * 1000000

def find_nemo(array):
    # t0 = time.perf_counter()
    for i in range(len(array)):
        if array[i] == "nemo":
            print("Found Nemo!")
    # elapsed_time = time.perf_counter() - t0
    print(f"Elapsed time: {elapsed_time} seconds")

find_nemo(nemo)
find_nemo(names) # O(N) --> Linear Time