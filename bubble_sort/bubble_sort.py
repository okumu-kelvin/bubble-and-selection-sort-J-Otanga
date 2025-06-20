# Bubble sort function that sorts the list step by step
def bubble_sort(data):
    n = len(data)  # Get the number of items in the list

    # Loop through the list multiple times
    for i in range(n):

        # Go through the unsorted part of the list
        for j in range(0, n - i - 1):

            # If the current number is bigger than the one next to it, swap them
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data  # Give back the sorted list


# My list that I want to sort
data = [5, 3, 2, 4, 4, 1]

# Call the function to sort it
sorted_array = bubble_sort(data)

# Print the sorted version
print("Sorted array is:", sorted_array)
