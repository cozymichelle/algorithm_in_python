'''
Find a min cut of an undirected graph, using Karger's random contraction algorithm

input: adjacency list
	E.g. "1	9	4" means that node 1 is connected to node 9 and 4.
output: min cut
'''
import numpy as np
import sys

class Graph:
	def __init__(self, filename):
		text_file = open(filename, 'r')
		self.adjacency_list = {int(line.split()[0]): sorted([int(entry) for entry in line.split()[1:]]) for line in text_file.readlines()}
		
	def reset_lists(self):
		adjacency_list = self.adjacency_list
		self.edge_list = []
		for key in adjacency_list:
			for node in adjacency_list[key]:
				if node > key:
					self.edge_list.append([key,node])
		self.node_list = [key for key in adjacency_list]
		self.node_mapping = {key: key for key in adjacency_list}
		
	def contract(self):
		edge_list = self.edge_list
		node_list = self.node_list
		node_mapping = self.node_mapping
		
		#### pop random edge from edge_list ####
		rand_num = np.random.randint(len(edge_list))
		rand_edge = edge_list.pop(rand_num)
		
		#### merge ####
		# first, pop node_list
		node_list.remove(rand_edge[-1])
			#pop the latter of rand_egde from the node_list
		
		# second, adjust node_mapping
		node_mapping[rand_edge[-1]] = rand_edge[0]
		
		# third, adjust edge_list
		self_loop = list()
		for i, edge in enumerate(edge_list):
			if edge[0] < rand_edge[-1]:
				if edge[1] == rand_edge[-1]:
					edge[1] = rand_edge[0]
					edge.sort()
					if edge[0] == edge[1]:
						self_loop.append(i)
			elif edge[0] == rand_edge[-1]:
				edge[0] = rand_edge[0]
				
		# fourth, remove self-loop
		self_loop.sort()
		for i in reversed(self_loop):
			edge_list.pop(i)
		
if __name__=='__main__':	
	try:
		filename = sys.argv[1]
	except IndexError:
		print("input file was not given")
		sys.exit()
		
	graph = Graph(filename)
	graph.reset_lists()
	min_cut = len(graph.edge_list)

	for num_iter in range(len(graph.node_list)**2):
		graph.reset_lists()
		while(len(graph.node_list)>2):
			graph.contract()
		if len(graph.edge_list) < min_cut:
			min_cut = len(graph.edge_list)
	
	print(min_cut)