# coding: utf-8
from __future__ import print_function


def heapify(arr, index, heap_size):
    """
    heapify the heap
        :param arr: array data
        :param index: the element index
        :param heap_size: the size of heap
    """
    largest = index
    left_index, right_index = 2 * index + 1, 2 * index + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, heap_size)



def heap_sort(arr):
    """
    the function of sorting the heap
        :param arr: array data
    """
    if not isinstance(arr, list) or len(arr) == 0:
        return
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    heap_sort(unsorted)
    print(unsorted)