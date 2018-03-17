'''
compute SCCs of a directed graph
usihng Kosaraju's Two-Pass Algorithm

input: ex. 1	2 => 1->2
output: sizes of the 5 largest SCCs in decreasing order

algrithm:
1. Create G_rev = G with the reversed direction of edges
2. Do DFS-loop on G_rev
3. Let G_time be a graph with node numbers replaced with its finishng time and edges reversed back.
4. Do DFS-loop on G_time

(DFS-loop calls for an iterative DFS, which uses stack)
''' 
import sys
import numpy as np

class Graph:
	def __init__(self, filename):
		# load data from input file
		self.edge_data = np.loadtxt(filename)
		self.n_vertices = len(np.unique(self.edge_data))	# no. of nodes
		
		# array for finishing time
		self.finish_time = np.zeros(self.n_vertices)
		
		# array to save the leader of each vertices
		self.leader = np.zeros(self.n_vertices)
		
	
	def top5SCC(self):
		### return top 5 sizes of SCCs ###
		_, SCC_sizes = np.unique(self.leader, return_counts=True)
		SCC_sizes[::-1].sort()	#sort in descending order
		
		if len(SCC_sizes) < 5:
			top5 = np.zeros(5)
			top5[:len(SCC_sizes)] = SCC_sizes
			return top5
		else:
			return SCC_sizes[:5]
	
	
	def DFSloop_Grev(self):
		### Run DFS-Loop on Grev ###		
		self.t = 0	# number of nodes processed so far
		self.path = []	# stores all the vertices visited at one DFS call
		
		self.reset_explored()
		self.create_Grev()
		
		# Do DFS from n downto 1 if and only if not yet explored
		for v in range(self.n_vertices, 0, -1):
			if not self.explored[int(v-1)]:
				self.stack.append(v)	# push current vertex to stack
				self.DFS(self.Grev, True)
				
				
	def DFSloop_Gtime(self):
		### Run DFS-Loop on G ###		
		self.s = 0	# current source vertex
		
		self.reset_explored()
		self.create_Gtime()
		
		# Do DFS from n downto 1 if and only if not yet explored
		for v in range(self.n_vertices, 0, -1):
			if not self.explored[int(v-1)]:
				self.stack.append(v)	# push current vertex to stack
				self.s = v	# set current vertex as its leader
				self.DFS(self.Gtime, False)
	
	
	def DFS(self, graph, reverse):
		### Run DFS ###
		# reverse: true if DFS for Grev
		
		stack = self.stack
		path = self.path
		explored = self.explored
		
		while stack:
			vertex = stack.pop()
			if explored[int(vertex-1)]:
				# if vertex was already explored, then continue
				continue
				
			if reverse:
				path.append(vertex)
				
			# mark current vertex as explored
			explored[int(vertex-1)] = 1
			
			# explore unexplored adjacent vertices of the current vertex
			if vertex in graph:
				for vtx in graph[vertex]:
					if not explored[int(vtx-1)]:
						stack.append(vtx)
			
			if not reverse:
				# set the leader of the current vertex
				self.leader[int(vertex-1)] = self.s
				
		# set the finishing time of vertices visited at current DFS call
		if reverse:	
			for p_idx in range(len(path), 0, -1) :
				self.t += 1
				self.finish_time[int(path[p_idx-1]-1)] = self.t
			del path[:]
		
		
	def reset_explored(self):
		# stack that pushes adjacent vertices to visit next
		self.stack = [self.n_vertices]
		# boolean array for tracking explored vertices
		self.explored = np.zeros(self.n_vertices)
		
		
	def create_Grev(self):
		# Grev is a dictionary which has a vertex as a key and its adjacent vertices as list
		# The direction of edges from the original G is reversed
		self.Grev = dict()
		for e1, e2 in self.edge_data:
			if e2 not in self.Grev:
				self.Grev[e2] = list()
			self.Grev[e2].append(e1)
			
			
	def create_Gtime(self):
		# Gtime is a dictionary which has a vertex as a key and its adjacent vertices as list
		# Replaces a vertex with its finishing time
		# The edges have the same direction as the original G
		finish_time = self.finish_time
		self.Gtime = dict()
		for e1, e2 in self.edge_data:
			if finish_time[int(e1-1)] not in self.Gtime:
				self.Gtime[finish_time[int(e1-1)]] = list()
			self.Gtime[finish_time[int(e1-1)]].append(finish_time[int(e2-1)])



if __name__=='__main__':
	try:
		filename = sys.argv[1]
	except IndexError:
		print("input file was not given")
		sys.exit()
	
	graph = Graph(filename)
	graph.DFSloop_Grev()
	graph.DFSloop_Gtime()
	print(graph.top5SCC())
