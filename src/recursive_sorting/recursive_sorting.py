# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print(arrA, arrB)
    merged_arr = []
    
    # TO-DO
    l = 0
    r = 0
    while l < len(arrA) and r < len(arrB):
        if arrA[l] < arrB[r]:
            merged_arr.append(arrA[l])
            l+=1
        else: 
            merged_arr.append(arrB[r])
            r+=1

    while l < len(arrA):
        merged_arr.append(arrA[l])
        l+=1

    while r < len(arrB):
        merged_arr.append(arrB[r])
        r+=1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    arr_length = len(arr)
    if arr_length <= 1:
        return arr

    midpoint = arr_length//2
    arrA, arrB = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(arrA, arrB)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
print(merge_sort([1, 5, 8, 4, 2, 6, 9, 6, 0, 3, 7]))