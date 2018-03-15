'''
Count comparisons in QuickSort
Choose a pivot, which appears in Partition, as the median among the leftmost, middle, and rightmost elements of the given array
Do not count comparisons done finding the median

input: integer array text file
	Example: array [5, 1, 4, 3] written in a file as:
		5
		1
		4
		3
output: count, sorted array
'''
import numpy as np
import sys

# load integer array file to the variable called 'data'
try:
	filename = sys.argv[1]
except IndexError:
	print("input file was not given")
	sys.exit()

data = np.loadtxt(filename)

def getMedian(arr, left, right):
	mid = (right-left)//2 + left
	med_idx = 0
	if arr[left]<arr[mid]:
		if arr[mid]<arr[right]:
			med_idx = mid
		else:
			if arr[left]<arr[right]:
				med_idx = right
			else:
				med_idx = left
	else:
		if arr[right]<arr[mid]:
			med_idx = mid
		else:
			if arr[right]<arr[left]:
				med_idx = right
			else:
				med_idx = left
	return med_idx
	
def Partition(arr, left, right):
	p_idx = getMedian(arr, left, right)
	pivot = arr[p_idx]
	
	if(p_idx != left):
		arr[p_idx], arr[left] = arr[left], arr[p_idx]
		
	i = left+1
	for j in range(left+1, right+1):
		if (arr[j] < pivot):
			if (i != j):
				arr[j], arr[i] = arr[i], arr[j]
			i += 1
	arr[left], arr[i-1] = arr[i-1], arr[left]
	return (right-left), i-1
	
def QuickSort(arr, left, right):
	count = 0
	if left<right:
		count, idx = Partition(arr, left, right)
		count += QuickSort(arr, left, idx-1)
		count += QuickSort(arr, idx+1, right)
	return count

if __name__=='__main__':
	cnt = QuickSort(data, 0, len(data)-1)
	print(cnt, data)