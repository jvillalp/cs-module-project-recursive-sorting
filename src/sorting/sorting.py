# TO-DO: complete the helper function below to merge 2 sorted arrays
# a = [1,5,10,15]
# b = [16, 20]
# [1,2,3,5,10,12,14,15,19]
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a_index, b_index, result_index = 0, 0, 0
    while result_index < elements:
        if a_index > len(arrA) - 1 or (b_index <= len(arrB) -1 and arrA[a_index] > arrB[b_index]):
            merged_arr[result_index] = arrB[b_index]
            b_index += 1
        else:
            merged_arr[result_index] = arrA[a_index]
            a_index += 1
        result_index += 1

    # Your code here
    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    
    #if a of len(arrA) > b of len(arrB)




    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
#     # Your code here
    if len(arr) <= 1:  # base case
        return arr

    # divide array in half and merge sort recursively
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

