import time

names = ["sep"] * 5
names.append("nemo")
names.extend(["sep"] * 5)


def find_nemo(array):
    for i in range(len(array)):
      print("Running")
      if array[i] == "nemo":
        print("Found Nemo!")
        break;
        # if we do not put break, it will iterate all the array even though it finds Nemo!