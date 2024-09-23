# What is the Big O of the below function? (Hint, you may want to go line by line)
def funChallenge(input):
  a = 10 # O(1)
  a = 50 + 3 # O(1)

  for i in range(len(input)): #O(N)
    anotherFunction() # O(N)
    stranger = True; # O(N)
    a = a + 1 # O(N)
  print(a)

# Guess it is O(N)
# 1 + 1+ N + N + N + N + 1 >> 3 + 4N >> O(N)