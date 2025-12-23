from typing import List
import random

# inplace version more ifficient
def quick_sort_inplace(arr: List[int], low: int, high: int):
    if low < high:
        p=partition(arr,low,high)
        quick_sort_inplace(arr,low,p-1)
        quick_sort_inplace(arr,p+1,high)

def partition(arr:List,low:int,high:int):
    pivot = high 
    i = low-1
    for j in range(low,high):
        if arr[j]<arr[pivot]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1


l = [2, 1, 4, 3, 5, 6, 9]
quick_sort_inplace(l, 0, len(l) - 1)
print(l)
