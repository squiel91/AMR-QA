from collections import defaultdict

# representation of a graph that allows labeling (optional) and reentrancy 

class Graph:
	def __init__(self):
		self.nodes = defaultdict(list)
		self.root = None

	def add_node(self, node):	
		self.nodes[node] = self.nodes[node]
		if not self.root:
			self.root = node

	def nodes(self):
		return self.nodes.keys() 

	def add_edge(self, origin, destination, label=None):
		self.add_node(origin)
		self.add_node(destination)
		adjacency = destination
		if label:
			adjacency = (label, destination)
		self.nodes[origin].append(adjacency)

	def adjacents(self, origin):
		return self.nodes[origin]

	def show(self):
		if self.root:
			self.show_recursively(self.root, [], 0)
			
	def show_recursively(self, node, visited, level, lable=''):
		if node not in visited:
			visited.append(node)
			if len(lable) > 0: lable += ' '
			print(' ' * level * 2 + lable + node)
			for adjacency in self.adjacents(node):
				adjacent_node = None
				label = None
				if type(adjacency) == tuple:
					label, adjacent_node = adjacency
				else:
					adjacent_node = adjacency
				visited = self.show_recursively(adjacent_node, visited, level + 1, label)
			return visited

# # tests	
# graph = Graph()
# graph.add_edge("p / picture", "i / it", ":domain")
# graph.add_edge("p / picture", "b2 / boa", ":topic")
# graph.add_edge("b2 / boa", "c2 / constrictor", ":mod") 
# graph.add_edge("b2 / boa", "s / swallow-01", ":ARG0-of") 
# graph.add_edge("s / swallow-01", "a / animal", ":ARG1") 

# graph.show()

