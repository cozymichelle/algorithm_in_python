# Linear search of an array
#
# Input:
#  - arr: a given array
#  - x : an element to find
#
# Output: index of the element x

def lsearch(arr, x):
    n = len(arr)
    for i in range(n):
        if(arr[i] == x):
            return i
    return -1

arr = [5, 1, 2, 4, 3]

# worst case scenario
x = 3
print(x, " is present at index ", lsearch(arr, x))

# best case scenario
y = 5
print(y, " is present at index ", lsearch(arr, y))