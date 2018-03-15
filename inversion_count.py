'''
Count inversions of an 1-d integer array using merge sort

input: integer array text file
	Example: array [5, 1, 4, 3] written in a file as:
		5
		1
		4
		3
output: sorted array, number of inversions

algorithm: given array A and its length n
	sortNcount(A, n)
	if n=1, return 0
	else
		arr1, cnt1 = sortNcount(A[:n/2], n/2)
		arr2, cnt2 = sortNcount(A[n/2:], n/2)
		arr3, cnt3 = mergeNcountSplitInv(A, n)
	return cnt1+cnt2+cnt3
	
runtime: O(n*log(n))
'''

import numpy as np
import sys

def sortNcount(arr):
	n = len(arr)
	if n==1:
		return arr, 0
	else:
		arr1, x = sortNcount(arr[:n//2])
		arr2, y = sortNcount(arr[n//2:])
		arr3, z = mergeNcountSplitInv(arr1, arr2, n)
		return arr3, x+y+z

def mergeNcountSplitInv(sorted1, sorted2, num):
	i=0
	j=0
	splitInv = 0
	sorted = np.zeros(num)

	for k in range(num):
		if (i==len(sorted1)):
			sorted[k:] = sorted2[j:]
			break
		elif (j==len(sorted2)):
			sorted[k:] = sorted1[i:]
			break
		else:
			if (sorted1[i] < sorted2[j]):
				sorted[k] = sorted1[i]
				i += 1
			elif (sorted2[j] < sorted1[i]):
				sorted[k] = sorted2[j]
				splitInv += len(sorted1) - i
				j += 1
	return sorted, splitInv
	
if __name__=='__main__':
	try:
		filename = sys.argv[1]
	except IndexError:
		print("input file was not given")
		sys.exit()

	data = np.loadtxt(filename)
	print(sortNcount(data))