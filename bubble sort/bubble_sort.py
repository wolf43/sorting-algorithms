"""This module implements bubble sort - https://en.wikipedia.org/wiki/Bubble_sort."""
import time
import random


def generate_random_list(size_of_list):
    """Generate a list of random values(between 1 and 1,000,000) of size size_of_list(<1,000,000)."""
    return random.sample(range(1, 1000000), size_of_list)


def is_swap_required(value1, value2):
    """Compare two values and decide is a swap is required."""
    if value1 <= value2:
        return False
    else:
        return True


def swap_values(list_containing_values, index_value1, index_value2):
    """Swap positions for value1 and value2."""
    list_containing_values[index_value1], list_containing_values[index_value2] = list_containing_values[index_value2], list_containing_values[index_value1]
    # Return the new list constructed in the function, yep that's how python lists work in functions
    return list_containing_values


def bubble_sort(list_containing_values):
    """Sort the list using bubble sort."""
    # Loop for iterations of compare of swap passes to sort
    for i in range(1, len(list_containing_values)):
        # Stop the looping early is list is sorted
        no_more_swaps = True
        # Loop over unsorted list, like a native https://www.youtube.com/watch?v=EnSu9hHGq5o
        for index, value in enumerate(list_containing_values):
            if index < len(list_containing_values) - i:
                if is_swap_required(value, list_containing_values[index + 1]):
                    swap_values(list_containing_values, index, index + 1)
                    no_more_swaps = False
        if no_more_swaps:
            break
    return list_containing_values


def bubble_sort_on_random_unsorted_list(size_of_list):
    """Run bubble sort on a random unsorted list."""
    # Generate a list using https://docs.python.org/2/library/random.html#random.sample
    my_list = generate_random_list(size_of_list)
    print('Original list:', my_list)

    # Get start time to measure performance - https://docs.python.org/3/library/time.html#time.process_time
    start_time = time.process_time()

    # Sort the list
    sorted_my_list = bubble_sort(my_list)

    # Get time taken to perform sorting
    time_to_run = time.process_time() - start_time

    # Print the results
    print('After bubble sort:', sorted_my_list)
    print('Time to run bubble sort on random unsorted list:', time_to_run)


def bubble_sort_on_sorted_list(size_of_list):
    """Run bubble sort on a sorted list."""
    # Generate a list using https://docs.python.org/2/library/random.html#random.sample
    my_list = list(range(size_of_list))
    print('Original list:', my_list)

    # Get start time to measure performance - https://docs.python.org/3/library/time.html#time.process_time
    start_time = time.process_time()

    # Sort the list
    sorted_my_list = bubble_sort(my_list)

    # Get time taken to perform sorting
    time_to_run = time.process_time() - start_time

    # Print the results
    print('After bubble sort:', sorted_my_list)
    print('Time to run bubble sort on sorted list:', time_to_run)
    print('This would be closer to unsorted list time if we didnt use check for no more swaps')


def main():
    """The main function."""
    bubble_sort_on_random_unsorted_list(5000)
    bubble_sort_on_sorted_list(5000)
    # Increase the number to a high value(5000) to see the O(n2) increase for bubble sort for random unsorted list

if __name__ == '__main__':
    main()
