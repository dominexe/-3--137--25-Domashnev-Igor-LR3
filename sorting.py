import logging
from log import *
import random

py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)
py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
py_handler.setFormatter(py_formatter)
py_logger.addHandler(py_handler)
py_logger.info(f"Testing the custom logger for module {__name__}...")


# Пузырьковая сортировка
def bubble_sort(nums):
    fl = True
    while fl:
        fl = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                fl = True

list = [6,7,2,9,5]
bubble_sort(list)
copy_list = [6,7,2,9,5]
test_division(copy_list,list)
py_logger.info(f"Call test_division with list {copy_list,list}")


# Проверка работы логера с несортированным листом
list_1 = [6,7,2,9,6]
test_division(list_1,list)
py_logger.info(f"Call test_division with list {list_1,list}")

# Сортировка выборкой
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
list = [12, 8, 3, 20, 11]
selection_sort(list)
copy_list = [12, 8, 3, 20, 11]
test_division(copy_list,list)
py_logger.info(f"Call test_division with list {copy_list,list}")



# Сортировка вставками
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

list = [9, 1, 15, 28, 6]
insertion_sort(list)
copy_list = [9, 1, 15, 28, 6]
test_division(copy_list,list)
py_logger.info(f"Call test_division with list {copy_list,list}")


# Пирамидальная сортировка
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


list = [35, 12, 43, 8, 51]
heap_sort(list)
copy_list = [35, 12, 43, 8, 51]
test_division(copy_list,list)
py_logger.info(f"Call test_division with list {copy_list,list}")

# Сортировка слиянием
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

list = [120, 45, 68, 250, 176]
list = merge_sort(list)
copy_list = [120, 45, 68, 250, 176]
test_division(copy_list,list)
py_logger.info(f"Call test_division with list {copy_list,list}")

# Быстрая сортировка
sp=[]
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

list = [22, 5, 1, 18, 99]
quick_sort(list)
copy_list = [22, 5, 1, 18, 99]
test_division(copy_list,list)
py_logger.info(f"Call test_division with list {copy_list,list}")
