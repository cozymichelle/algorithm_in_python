'''
Binary Search

Input:
 - arr: a given sorted array
 - x: an element to find
 - l: the leftmost index of arr
 - r: the rightmost index of arr
Output: index of the element x
'''

# Recursive binary search
def rec_binsearch(arr, x, l, r):
    if (l > r or r < l): # if index out of bound
        return -1

    n = r - l + 1       # size of the array from l to r
    i = l + n // 2      # the index of the middle of arr

    if x == arr[i]:
        return i
    elif x < arr[i]: # search left half
        return rec_binsearch(arr, x, l, i-1)
    elif x > arr[i]: # search right half
        return rec_binsearch(arr, x, i+1, r)

# Iterative binary search
def itr_binsearch(arr, x, l, r):
    while (l <= r):
        i = l + (r - l + 1) // 2
        if x == arr[i]:
            return i
        elif x < arr[i]:
            r = i - 1
        elif x > arr[i]:
            l = i + 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
x = 3
print(x, " is present at index ", rec_binsearch(arr, x, 0, len(arr)-1))
print(x, " is present at index ", itr_binsearch(arr, x, 0, len(arr)-1))
