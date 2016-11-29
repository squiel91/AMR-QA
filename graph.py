from collections import defaultdict

# representation of a graph that allows labeling (optional) and reentrancy 

class Graph:

	def __init__(self):
		self.nodes = defaultdict(list)
		self.root = None
		self.unique_id = 1000

	def add_node(self, node):	
		self.nodes[node] = self.nodes[node]
		if not self.root:
			self.root = node

	def remove_node(self, node):
		for node_iter in self.nodes.keys():
			if get_value(node_iter) == node:
				del self.nodes[node_iter]
				break

	def update_destination(self, node_old, node_new):
		for node in self.nodes.keys():
			node_adjacents = self.nodes[node]
			new_node_adjacents = []
			for adjacency in node_adjacents:
				new_adjacent_node = adjacency
				if type(adjacency) == tuple:
					label, adjacent_node = adjacency
					if get_value(adjacent_node) == node_old:
						new_adjacent_node = (label, node_new)
				else: 
					if get_value(adjacency) == node_old:
						new_node_adjacents = node_new
				new_node_adjacents.append(new_adjacent_node)
			self.nodes[node] = new_node_adjacents

	def get_nodes(self):
		return [get_value(node) for node in self.nodes.keys()]

	# terminal means that destination will be a fixed leaf: wont have childs 
	# and origin will be its only parent
	def add_edge(self, origin, destination, label=None, terminal=False):
		if terminal:
			destination += "|terminal|" + str(self.unique_id)
			self.unique_id += 1
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
			print(' ' * level * 2 + lable + node.split("|terminal|")[0])
			for adjacency in self.adjacents(node):
				adjacent_node = None
				label = None
				if type(adjacency) == tuple:
					label, adjacent_node = adjacency
				else:
					adjacent_node = adjacency
				visited = self.show_recursively(adjacent_node, visited, level + 1, label)
		return visited

def get_value(value):
		return value.split('|terminal|')[0]

