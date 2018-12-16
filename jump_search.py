'''
Jump Search

Input:
 - arr: a given sorted array
 - x: an element to find
 - m: number of elements to jump ahead
Output: index of the element x

The optimal block size is m = sqrt(n).
worst case scenario: (n / m) jumps + (m - 1) comparisons
'''

def lin_search(arr, x, l, r):
    # do linear search on arr from index l to r
    # and find x
    for i in range(l, r + 1):
        if arr[i] == x:
            return i

    # if x not found
    return -1

def jump_search(arr, x, m):
    n = len(arr)    # size of the array arr

    # if block size is greater than the size of arr
    if m > n:
        return -1

    # if x is smaller than the min of arr
    # or x is greater than the max of arr
    if x < arr[0] or x > arr[n - 1]:
        return -1

    jump = 0        # index to where we jump forward
    while arr[jump] <= x:
        if arr[jump] == x:  # found x
            return jump

        prev = jump # index before jump
        jump += m
        jump = min(jump, n-1)

    # do linear search
    return lin_search(arr, x, prev + 1, jump - 1)

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(jump_search(arr, 56, 4))