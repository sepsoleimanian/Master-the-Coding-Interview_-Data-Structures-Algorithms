def reverse(input_str):
    if not isinstance(input_str, str) or len(input_str) < 2:
        print("Wrong Input")
        return
    
    reversed_str = []
    
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str.append(input_str[i])
    
    # Join the list back into a string and print the result
    print(''.join(reversed_str))

# Example usage:
word = "Hi My Name Is Sepideh"
reverse(word)

# O(n)