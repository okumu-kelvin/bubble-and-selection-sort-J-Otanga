def selection_sort(arr):
    n = len(arr)
    # Go through each item in the list except the last one
    for i in range(n - 1):
        min_index = i  # Assume the current item is the smallest
        # Look through the rest of the list to find something smaller
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Found a new smallest number, update min_index
        # Swap the smallest number found with the one at position i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# List of numbers I want to sort
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

# Run my sorting function
selection_sort(my_array)

# Print the final sorted list
print("Sorted array:", my_array)
