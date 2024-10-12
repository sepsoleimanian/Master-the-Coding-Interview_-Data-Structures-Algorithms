def print_all_numbers_then_all_pair_sums(numbers):
    print("These are the numbers:") 
    for number in numbers: # O(N)
        print(number)
    
    print("And these are their sums:")
    # you don’t need to use range() when iterating directly over a list.
    for first_number in numbers:
        for second_number in numbers:
            print(first_number + second_number) # O(N^2)

numbers = [1, 2, 3, 4, 5]
print_all_numbers_then_all_pair_sums(numbers)
# O(N) + O(N^2) --> O(N^2)
