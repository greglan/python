# -*- coding: utf-8 -*-

from algorithms.sorting.utils import *


def merge_sort(unsorted_list):
    n = len(unsorted_list)
    operations = Complexity()

    if n <= 1:
        return unsorted_list, operations
    else:
        middle = n // 2
        left, left_ops = merge_sort(unsorted_list[:middle])
        right, right_ops = merge_sort(unsorted_list[middle:])

        operations.comparisons = left_ops.comparisons + right_ops.comparisons

        n = len(left)
        m = len(right)
        p, q = 0, 0
        sorted_list = []

        while p < n and q < m:
            operations.comparisons += 3
            if left[p] < right[q]:
                sorted_list.append(left[p])
                p += 1
            else:
                sorted_list.append(right[q])
                q += 1

        operations.comparisons += 1
        if p < n:
            sorted_list = sorted_list + left[p:]

        operations.comparisons += 1
        if q < m:
            sorted_list = sorted_list + right[q:]

        return sorted_list, operations
