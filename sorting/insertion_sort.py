from typing import List


def insertion_sort(arr: List) -> List:

    for i in range(1, len(arr)):
        j = i - 1

        while j >= 0 and arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1

    return arr
