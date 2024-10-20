"""
There always is a trade off between Time complexity and Space Complexity.
When a program execute, it has two ways to remember things:
1) Heap
2) Stack
 
Heap: Variables
Stack: Function calls
"""
def booo(n):
  for i in range(len(n)):
    print("boooo!")

booo([1,2,3,4,5])

"""
Space Complexity:
we do not care about input size
"""
def array_of_hi_n_times(n):
  hi_array = []
  for i in range(n):
    hi_array.append("Hi")
  print(hi_array)
  return hi_array;

array_of_hi_n_times(6)

"""
Space Complexity:
we created variable(i) and data structure(list) => O(N)

Space complexity is about definition of function and how it works.
"""