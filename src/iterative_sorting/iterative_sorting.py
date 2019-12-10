# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             
        for x in range(i+1, len(arr)):
         # select the presently exposed smallest item, and cache that smallest item for continuous comparison with the rest of the list
            if arr[x] < arr[smallest_index]:
                smallest_index = x


        # TO-DO: swap
        if smallest_index != i:
            arr[smallest_index], arr[cur_index] = arr[cur_index],arr[smallest_index]
    print(arr)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # set state for swapping status
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
             # if pair[1] > pair[0], swap them. 
              # This will progressively transfer larger items to end of list
            if arr[i]> arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                 # a swap was made, so inform the algorithm to not break early
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr