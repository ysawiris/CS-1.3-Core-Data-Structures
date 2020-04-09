#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    
    #check if we have exceed the length of the array
    if index >= len(array):
        return None
    
    #check if the current index is the item we are looking for 
    if array[index] == item:
        return index 

    #since the item has not be found,
    #recall the function, and add 1 to its index 
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0
    right = len(array) - 1 

    while left <= right:
        
        mid =   right + left // 2
    
        # Check if x is present at mid 
        if array[mid] == item: 
            return mid 
  
        # If x is greater, ignore left half 
        elif array[mid] < item: 
            left = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            right = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return None




def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
