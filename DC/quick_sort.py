import random
from typing import List


def quick_sort(arr: List) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = random.randrange(0, len(arr) - 1)
    pivot_val = arr.pop(pivot)
    less = [x for x in arr if x <= pivot_val]
    bigger = [x for x in arr if x > pivot_val]
    return quick_sort(less) + [pivot_val] + quick_sort(bigger)


l = [2, 1, 4, 3, 5, 6, 9]
print(quick_sort(l))