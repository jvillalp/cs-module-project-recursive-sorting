# # TO-DO: Implement a recursive implementation of binary search
# def binary_search(arr, target, start, end):
#     # Your code here

#     #iterative
#     start = 0
#     end = len(arr) -1

#     while start <= end:
#         middle = (start + end) // 2
#         guess = arr[middle]
#         if guess == target:
#             return middle
#         if guess > target:
#             end = middle +1 
#     return -1


def binary_search(arr, target, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2
    #if the element at the middle index of array == target, return this because it is the target
    if arr[middle] == target:
        return middle
        # if target is less than the element of the middle index
    elif target < arr[middle]:
        #return all things that are in start to middle-1 of target
        return binary_search(arr, target, start, middle-1)
        #return all things that are in middle+1 to end of target
    else:
        return binary_search(arr, target, middle+1, end)
        
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursiv
# ely 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
