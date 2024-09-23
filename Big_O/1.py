my_list = ["Nemo"]

def findNemo(array):
    for i in range(len(array)): 
        if array[i] == "Nemo":
            print("Found Nemo! :)")
            return 
    print("Nemo Not Found. :()") 

findNemo(my_list)  