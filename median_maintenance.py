'''
median maintenence algorithm, using heap

input: a sequance x1, ..., xn of numbers, one-by-one
median maintenance: at each time step i, get the median of {x1, ..., xi}
output: (the sum of n medians) mod 10000

Takes advantage of two heaps heap_low and heap_high, 
where small half values and large half values are stored respectively.
heap_low is a max heap and heap_high is a min heap.
The size of heap_low and heap_high is always ~n/2.
'''
import numpy as np
import math
import sys

class MedianMaintenance:
	def __init__(self, filename):
		self.num_sequence = np.loadtxt(filename)
		self.heap_low = Heap(-1)	# max heap for small half values
		self.heap_high = Heap(1)	# min heap for large half values
		
	def get_median(self, input):
		heap_low = self.heap_low
		heap_high = self.heap_high
		
		# base case: when both heaps are empty
		if not heap_low.heap:
			heap_low.insert_node(input)
			return input
			
		if input < heap_low.heap[0]:
			heap_low.insert_node(input)
			if len(heap_low.heap) - len(heap_high.heap) == 2:
				heap_high.insert_node(heap_low.extract_root())
		else:
			heap_high.insert_node(input)
			if len(heap_low.heap) < len(heap_high.heap):
				heap_low.insert_node(heap_high.extract_root())
				
		return heap_low.heap[0]
		

class Heap:
	def __init__(self, min):
		self.heap = []
		self.min = min	# 1 if min-heap, -1 if max-heap
		
	def swap_nodes(self, idx1, idx2):
		self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
	
	def insert_node(self, key):
		# insert node to the end of heap
		heap = self.heap
		heap.append(key)
		
		key_idx = len(heap)-1
		parent = heap[(key_idx-1)//2]
		
		# bubble-up
		while (self.min*(parent-key) > 0 and key_idx>0):
			# if heap property is not met, swap with its parent
			self.swap_nodes(key_idx, (key_idx - 1)//2)
			key_idx = (key_idx-1)//2
			parent = heap[(key_idx-1)//2]
	
	def extract_root(self):
		heap = self.heap
		
		# base case: when there is one element in heap
		if len(heap) == 1:
			return heap.pop()
		
		# swap last leaf and root
		# then extract min (or max), which is now located at the last leaf	
		self.swap_nodes(0, len(heap)-1)
		old_root = heap.pop()		
		new_root = heap[0]
		root_idx = 0
		
		# bubble down
		while 2*(root_idx+1) <= len(heap):
			left_child = 2*root_idx+1
			right_child = -1 if left_child+1==len(heap) else left_child+1
			if right_child == -1 or \
			self.min * (heap[left_child] - heap[right_child]) < 0:
				smaller_child = left_child
			else:
				smaller_child = right_child
					
			if self.min*(new_root - heap[smaller_child]) > 0:
				self.swap_nodes(root_idx, smaller_child)
			root_idx = smaller_child
				
		return old_root

		
if __name__=='__main__':
	try:
		filename = sys.argv[1]
	except IndexError:
		print("input file was not given")
		sys.exit()

	data = MedianMaintenance(filename)
	med_sum = 0
	for i in range(len(data.num_sequence)):
		median_i = data.get_median(int(data.num_sequence[i]))
		print('median: ',median_i)
		med_sum += median_i
	print(med_sum%10000)
		
