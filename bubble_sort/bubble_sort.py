# Bubble sort function that sorts the list step by step
def bubble_sort(unsorted_list):
    n = len(unsorted_list)  # Get the number of items in the list

    # Loop through the list multiple times
    for i in range(n):

        # Go through the unsorted part of the list
        for j in range(0, n - i - 1):

            # If the current number is bigger than the one next to it, swap them
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

    return unsorted_list  # Give back the sorted list
def reverse_array(arr):
    return arr[::-1]  

# My list that I want to sort

arr = [5, 3, 2, 4, 4, 1]
# Call the function to sort it
sorted_array = bubble_sort(arr)
# Print the sorted version
print("Sorted array is:", sorted_array)
# Print the reversed version
print("Reversed array is:",reverse_array(arr) )  # Should show the list backwards
