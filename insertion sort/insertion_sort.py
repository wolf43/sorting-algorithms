"""This module implements insertion sort."""
import time
import random


def generate_random_list(size_of_list):
    """Generate a list of random values(between 1 and 1,000,000) of size size_of_list(<1,000,000)."""
    return random.sample(range(1, 1000000), size_of_list)


def insertion_sort(list_to_sort):
    """Sort the list using insertion sort."""
    for index in range(1, len(list_to_sort)):
        currentvalue = list_to_sort[index]
        position = index
        while position > 0 and list_to_sort[position - 1] > currentvalue:
            list_to_sort[position] = list_to_sort[position - 1]
            position = position - 1
            # print('Inside while:', list_to_sort)

        list_to_sort[position] = currentvalue
    return list_to_sort


def insertion_sort_on_random_unsorted_list(size_of_list):
    """Run insertion sort on a random unsorted list."""
    # Generate a list using https://docs.python.org/2/library/random.html#random.sample
    my_list = generate_random_list(size_of_list)
    print('Original list:', my_list)

    # Get start time to measure performance - https://docs.python.org/3/library/time.html#time.process_time
    start_time = time.process_time()

    # Sort the list
    sorted_my_list = insertion_sort(my_list)

    # Get time taken to perform sorting
    time_to_run = time.process_time() - start_time

    # Print the results
    print('After insertion sort:', sorted_my_list)
    print('Time to run insertion sort on random unsorted list:', time_to_run)


def insertion_sort_on_sorted_list(size_of_list):
    """Run insertion sort on a sorted list."""
    # Generate a list using https://docs.python.org/2/library/random.html#random.sample
    my_list = list(range(size_of_list))
    print('Original list:', my_list)

    # Get start time to measure performance - https://docs.python.org/3/library/time.html#time.process_time
    start_time = time.process_time()

    # Sort the list
    sorted_my_list = insertion_sort(my_list)

    # Get time taken to perform sorting
    time_to_run = time.process_time() - start_time

    # Print the results
    print('After insertion sort:', sorted_my_list)
    print('Time to run insertion sort on sorted list:', time_to_run)


def main():
    """The main function."""
    insertion_sort_on_random_unsorted_list(5000)
    insertion_sort_on_sorted_list(5000)
    # Increase the number to a high value(5000) to see the O(n2) increase for sort for random unsorted list

if __name__ == '__main__':
    main()
