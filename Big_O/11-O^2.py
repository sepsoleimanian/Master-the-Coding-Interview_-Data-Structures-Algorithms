# Log all pairs of array
boxes = ["a","b","c","d","e","f"]

for i in range(len(boxes)):
  for j in range(len(boxes)):
    print(f"{boxes[i]}, {boxes[j]}")
# O(N^2)