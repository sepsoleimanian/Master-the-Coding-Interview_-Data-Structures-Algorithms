def merge_sorted_arrays(list1, list2):
  final_list = list1 + list2
  final_list.sort()
  print(final_list)



merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
#output: [0, 3, 4, 4, 6, 30, 31]