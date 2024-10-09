def funChallenge(input):
  a = 10 #O(1)
  a = 50 + 3 #O(1)

  for i in range(len(input)): #O(N)
    anotherFunction() #O(N)
    stranger = True  #O(N)
    a = a + 1  #O(N)

  return a #O(1)

funChallenge()
"""
Final Big(O) = 1 + 1 + 1 +  N + N + N + N = O(4N + 3) => O(N)
"""