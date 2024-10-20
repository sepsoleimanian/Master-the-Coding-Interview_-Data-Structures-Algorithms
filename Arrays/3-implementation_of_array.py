class MyList:
    def __init__(self, initial_capacity=1):
        self.capacity = initial_capacity  # Initial capacity of the list
        self.size = 0  # Current number of elements in the list
        self.array = self._create_array(self.capacity)  # Allocate memory for the list

    # Create an array of a given capacity (with None values)
    def _create_array(self, capacity):
        return [None] * capacity

    # Resize the array when it's full or when shrinking
    def _resize(self, new_capacity):
        new_array = self._create_array(new_capacity)
        for i in range(self.size):  # Copy all elements to the new array
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # Add an element to the end of the list
    def append(self, value):
        if self.size == self.capacity:  # If the array is full, resize it
            self._resize(2 * self.capacity)
        self.array[self.size] = value  # Add the new element
        self.size += 1

    # Remove an element by index
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):  # Shift elements to the left
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None  # Clear the last element
        self.size -= 1
        if self.size <= self.capacity // 4:  # Reduce capacity if needed
            self._resize(self.capacity // 2)

    # Get an element by index
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    # Return the current size of the list
    def get_size(self):
        return self.size

    # Print the current elements in the list
    def display(self):
        print("List:", [self.array[i] for i in range(self.size)])

    # Insert an element at a specific index
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:  # Resize if the array is full
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):  # Shift elements to the right
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    # Remove a specific element (first occurrence)
    def remove(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                self.remove_at(i)  # Use remove_at to remove by index
                return
        raise ValueError(f"{value} not found in list")

# Example usage:
my_list = MyList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.display()  # Output: List: [10, 20, 30]

my_list.insert(1, 15)
my_list.display()  # Output: List: [10, 15, 20, 30]

my_list.remove_at(2)
my_list.display()  # Output: List: [10, 15, 30]

print("Element at index 1:", my_list.get(1))  # Output: Element at index 1: 15

my_list.remove(15)
my_list.display()  # Output: List: [10, 30]