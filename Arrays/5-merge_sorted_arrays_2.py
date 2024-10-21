def merge_sorted_arrays(list1, list2):
    merged_array = []

    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1

    while len(list1) > 0 and len(list2) > 0:
        array_1_item = list1[0]  
        array_2_item = list2[0]

        if array_1_item < array_2_item:
            merged_array.append(array_1_item)
            list1.pop(0)  
        elif array_1_item > array_2_item:
            merged_array.append(array_2_item)
            list2.pop(0) 
        else:
            merged_array.append(array_1_item)
            merged_array.append(array_2_item)
            list1.pop(0)
            list2.pop(0)

    # If there are remaining elements in list1 or list2, extend the merged array with them
    if len(list1) > 0:
        merged_array.extend(list1)
    if len(list2) > 0:
        merged_array.extend(list2)

    return merged_array

result = merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
print(result)  