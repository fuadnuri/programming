from typing import List 
def merge(array1:List,array2:List):
    i,j=0,0
    size = len(array1)+len(array2)
    merged=[None for _ in range(size)]
    for k in range(size):
        if i>=len(array1):
            merged[k]=array2[j]
            j+=1
        elif j >= len(array2):
            merged[k] = array1[i]
            i+=1
        elif array1[i] <= array2[j]:
            merged[k] = array1[i]
            i+=1
        else:
            merged[k] = array2[j]
            j+=1
    return merged


def mergeSort(array:list)->list:
    if len(array)> 1:
        m = len(array)//2
        left = mergeSort(array[:m])
        right = mergeSort(array[m:])
        # print(f"left {array[:m]} right {array[m:]}")
        return merge(left,right)
    return array

test_list = [3,1,4,8]

print(mergeSort(test_list))
