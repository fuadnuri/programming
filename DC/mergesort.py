from typing import List


def merge_sort(arr: List) -> List:
    if len(arr) <= 1:
        return arr
    mid: int = len(arr) // 2

    left: List = merge_sort(arr[:mid])
    right: List = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []

    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left)
    merged.extend(right)

    return merged
