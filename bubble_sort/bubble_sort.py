def bubble_sort(unsorted_list):
    # Find out how many items are in the list
    n = len(unsorted_list)
    i = 0  # This will count how many passes we've done

    # Keep looping until we've gone through the list n times
    while i < n:
        j = 0  # Start comparing from the beginning of the list

        # Go through the list up to the last unsorted item
        while j < n - i - 1:
            # If the current item is bigger than the one next to it, swap them
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
            j += 1  # Move to the next pair

        i += 1  # One full pass done, move to the next round
    return unsorted_list  # Return the list once it's fully sorted

# My starting list (not sorted)
arr = [5, 4, 3, 2, 1, 0]

# Run the bubble sort function
sorted_arr = bubble_sort(arr)

# Print the sorted list
print("Sorted list:", sorted_arr)
