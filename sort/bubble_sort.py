# coding: utf-8

from __future__ import print_function


def bubble_sort(arr):
    """
    docstring here
        :param arr: array data
    """
    if not isinstance(arr, list) or len(arr) == 0:
        return
    length = len(arr)
    for i in range(length)[::-1]:
        is_sorted = True
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted is True:
            break
    

if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    bubble_sort(unsorted)
    print(unsorted)