'''
Implement Dijkstra's algorithm to find single-source shortest paths

input: adjacency list of an undirected weighted graph
	e.g. "1  5,11  8,3" means that there is an edge between vertex 1 and 5 and its weight is 11. 
	Also there is an edge between vertex 1 and 8 and its weight is 3.
output: vertex number, shortest distance from source, shortest path
	e.g. "2	1 [1, 2]" means that shortest distance from source vertex to vertex 2 is 1 and the path is "1(source)->2".

(Used min heap)
''' 
import math
import numpy as np
import heapq as hp
import argparse

# get argument
parser = argparse.ArgumentParser()
parser.add_argument("--file_dir", type=str, default="./dijkstraData.txt", help="directory of an input file")
parser.add_argument("--source", type=int, default=1, help="source vertex")
parser.add_argument("--terminal", type=int, default=1, help="terminal vertex")


class Graph:
	def __init__(self, filename):
		with open(filename) as f:
			# get adjacency list from input file
			# a dictionary with format {vertex: [adjacent vertex, weight]}
			self.adj_list = dict()
			for x in f:
				line = x.split('\t')
				self.adj_list[int(line[0])] = [[int(z) for z in y.split(',')] for y in line[1:-1]]
			
			n_vertices = len(self.adj_list)	# number of vertices
			self.processed = np.zeros(n_vertices)
				# boolean array to check whether a vertex is already processed
			self.shortest = dict()
				# dictionary to store shortest path info
				# {vertex: shortest distance, [shortest path from source]}
			self.dist_heap = MinHeap(n_vertices)
				# initialize MinHeap for shortest path
	
	
	def do_dijkstra(self, source):
		dist_heap = self.dist_heap
		processed = self.processed
		
		#initialize source vertex
		dist_heap.add_node(1,0,1)
		self.shortest[1] = (0,[])
		
		while dist_heap.minheap:	
			# extract min
			min_dist, min_vertex, prev_min = dist_heap.extract_min()
			
			if not processed[min_vertex-1]:
				processed[min_vertex-1] = 1
				self.shortest[min_vertex] = (min_dist, self.shortest[prev_min][1] + [min_vertex])
				
				# update shortest distances of the adjacent vertices of min_vertex
				min_alist = self.adj_list[min_vertex]
				for i in range(len(min_alist)):
					v = min_alist[i][0]
					v_weight = min_alist[i][1]
					
					if not processed[v-1]:
						dist_heap.add_node(v, min_dist+v_weight, min_vertex)
				
				dist_heap.min_heapify()
		
			
class MinHeap():
	def __init__(self, vertex_num):
		self.minheap = []
	
	def add_node(self, vertex_num, distance, prev_vnum):
		hp.heappush(self.minheap, [distance, vertex_num, prev_vnum])
		
	def min_heapify(self):
		hp.heapify(self.minheap)
			
	def extract_min(self):
		return hp.heappop(self.minheap)


if __name__=='__main__':
	args = parser.parse_args()
	graph = Graph(args.file_dir)
	graph.do_dijkstra(args.source)
	print(args.terminal, graph.shortest[args.terminal])