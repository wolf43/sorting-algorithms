"""This module implements selection sort."""
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


def find_index_of_smallest(list_of_values):
    """Find the index of smallest value in the list."""
    # The easiest way to do this is to use the min function, but this is a well implemented and messes up the O(n2) time
    return list_of_values.index(min(list_of_values))
    # this is the code for the more time consuming, non-pythonic way
    # for index, value in enumerate(list_of_values):
    #     if value <= min(list_of_values):
    #         return index


def selection_sort(list_to_sort):
    """Sort the list using selection sort."""
    for index1, _ in enumerate(list_to_sort):
        index_smallest = find_index_of_smallest(list_to_sort[index1:]) + index1
        if is_swap_required(list_to_sort[index1], list_to_sort[index_smallest]):
            swap_values(list_to_sort, index1, index_smallest)
    return list_to_sort


def selection_sort_on_random_unsorted_list(size_of_list):
    """Run selection sort on a random unsorted list."""
    # Generate a list using https://docs.python.org/2/library/random.html#random.sample
    my_list = generate_random_list(size_of_list)
    print('Original list:', my_list)

    # Get start time to measure performance - https://docs.python.org/3/library/time.html#time.process_time
    start_time = time.process_time()

    # Sort the list
    sorted_my_list = selection_sort(my_list)

    # Get time taken to perform sorting
    time_to_run = time.process_time() - start_time

    # Print the results
    print('After selection sort:', sorted_my_list)
    print('Time to run selection sort on random unsorted list:', time_to_run)


def selection_sort_on_sorted_list(size_of_list):
    """Run selection sort on a sorted list."""
    # Generate a list using https://docs.python.org/2/library/random.html#random.sample
    my_list = list(range(size_of_list))
    print('Original list:', my_list)

    # Get start time to measure performance - https://docs.python.org/3/library/time.html#time.process_time
    start_time = time.process_time()

    # Sort the list
    sorted_my_list = selection_sort(my_list)

    # Get time taken to perform sorting
    time_to_run = time.process_time() - start_time

    # Print the results
    print('After selection sort:', sorted_my_list)
    print('Time to run selection sort on sorted list:', time_to_run)


def main():
    """The main function."""
    selection_sort_on_random_unsorted_list(500)
    selection_sort_on_sorted_list(500)
    # Increase the number to a high value(5000) to see the O(n2) increase for sort for random unsorted list

if __name__ == '__main__':
    main()
