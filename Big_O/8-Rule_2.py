import math 

def printFirstItemThenFirstHalfThenSayHi10Times(items):
  print(items[0]) #O(1)

  middle_index = math.floor(len(items)/2)
  index = 0
  while index < middle_index: #O(N/2)
    print(items[index])
    index = index + 1

  for i in range(10): #O(1)
    print("Hi!")


list = [1,2,3,4,5,6,7,8,9,10]
printFirstItemThenFirstHalfThenSayHi10Times(list)    

# 1 + N/2 + 100 = 101 + N/2 --> O(N/2) --> O(N)