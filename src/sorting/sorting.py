# TO-DO: complete the helper function below to merge 2 sorted arrays
# a = [1,5,10,15]
# b = [16, 20]
# [1,2,3,5,10,12,14,15,19]
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    # starting at the beginning of `a` and `b`
    a_index, b_index, result_index = 0, 0, 0
    # compare the next value of each
    while result_index < elements:
        if a_index > len(arrA) - 1 or (b_index <= len(arrB) -1 and arrA[a_index] > arrB[b_index]):
    # add smallest to `merged_arr`
            merged_arr[result_index] = arrB[b_index]
            b_index += 1
        else:
            merged_arr[result_index] = arrA[a_index]
            a_index += 1
        result_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #if length of array is less than or equal to 1
    if len(arr) <= 1:  # base case
        return arr

    # divide array in half and merge sort recursively
    half = len(arr) // 2
    #left merge_sort first half
    left = merge_sort(arr[:half])
     #left merge_sort second half
    right = merge_sort(arr[half:])
    #return sorted left and right sides into one array
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

