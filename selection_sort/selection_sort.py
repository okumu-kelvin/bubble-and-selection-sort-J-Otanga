# Selection sort function that returns a sorted copy of the list
def selection_sort(arr):
    data = arr.copy()  # Make a copy so we don't mess up the original list
    n = len(data)  # Get how many items are in the list

    # Go through the list one item at a time
    for i in range(n):
        min_index = i  # Start by assuming the current item is the smallest

        # Look for something smaller in the rest of the list
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j  # Found something smaller, update min_index

        # Swap the smallest item found with the one at the current position
        data[i], data[min_index] = data[min_index], data[i]

    return data  # Return the new sorted list


# A list I want to sort
arr = [4, 3, 5, 1, 2]
sorted_array = selection_sort(arr)
print("Sorted array is:", sorted_array)  # Should show the numbers in order


# Function to reverse a list
def reverse_array(arr):
    return arr[::-1]  # This slices the list from end to start (basically flips it)


# A list I want to reverse
arr = [1, 2, 3, 4, 5]
reversed_array = reverse_array(arr)
print("Reversed array is:", reversed_array)  # Should show the list backwards
