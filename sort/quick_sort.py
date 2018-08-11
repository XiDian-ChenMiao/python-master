# coding: utf-8
from __future__ import print_function


def quick_sort(arr):
    """Pure implementation of quick sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    arr_len = len(arr)
    if(arr_len <= 1):
        return arr
    else:
        pivot = arr[0]
        greater = [element for element in arr[1:] if element > pivot]
        lesser = [element for element in arr[1:] if element <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


def partition(arr, left, right):
    """
    partition function to find a digit which is bigger than the front and is lesser than the backend.
        :param arr: array data
        :param left: left flag
        :param right: right flag
    """
    i, j = left, right
    pivot = arr[left]
    while (i != j):
        while (i != j and arr[j] > pivot):
            j = j - 1
        while (i != j and arr[i] <= pivot):
            i = i + 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[i] = arr[i], arr[left]
    return i


def quick_sort_v2(arr, left, right):
    """
    quciksort function of version 2 by moving elements
        :param arr: array data
        :param left: left flag
        :param right: right flag
    """
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort_v2(arr, left, pivot - 1)
        quick_sort_v2(arr, pivot + 1, right)


if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    result = quick_sort(unsorted)
    print(result)
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    quick_sort_v2(unsorted, 0, len(unsorted) - 1)
    print(unsorted)