from typing import List    
import random 
def quick_sort_randomized(arr:List[int],low:int,high:int):
    if low<high:
        p = random_partition(arr,low,high)
        quick_sort_randomized(arr,low,p-1)
        quick_sort_randomized(arr,p+1,high)

def random_partition(arr:List[int],low:int,high:int)->int:
    p = random.randrange(low,high)

    arr[p],arr[high]=arr[high],arr[p]

    return lamoto_partition(arr,low,high)

def lamoto_partition(arr:List,low:int,high:int)->int:
    i=low-1
    pivot=high 
    for j in range(low,high):
        if arr[j]<arr[pivot]:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    
    arr[i+1],arr[high]=arr[high],arr[i+1]

    return i+1


l = [2, 1, 4, 3, 5, 6, 9]
quick_sort_randomized(l, 0, len(l) - 1)
print(l)