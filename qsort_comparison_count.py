'''
Count comparisons in QuickSort

argument: 
	--left: True, if the leftmost element is used as a pivot in Partition
		False, if the rightmost element is used as a pivot

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
import argparse

# get argument
parser = argparse.ArgumentParser()
parser.add_argument("--left", default=False, action="store_true", help="use the leftmost element as a pivot")
parser.add_argument("--file_dir", type=str, default="./QuickSort.txt", help="directory of an input file")
args = parser.parse_args()

data = np.loadtxt(args.file_dir)

def Partition(arr, left, right):
	if args.left:
		# if left==True, set the leftmost element as a pivot
		pivot = arr[left]
	elif not args.left:
		# set the rightmost element as a pivot 
		# and swap it with the leftmost element
		pivot = arr[right]
		arr[right], arr[left] = arr[left], arr[right]
		
	i = left+1
	for j in range(left+1, right+1):
		if (arr[j] < pivot):
			if (i != j):
				arr[j], arr[i] = arr[i], arr[j]
			i += 1
	arr[left], arr[i-1] = arr[i-1], arr[left]
	return right-left, i-1


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