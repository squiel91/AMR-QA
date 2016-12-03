from collections import defaultdict

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

	def adjacents(self, origin, label=None):
		if not label:
			return search_ingnoring_vars(self.nodes, origin)
		else:
			for adjacency in search_ingnoring_vars(self.nodes, origin):
				if type(adjacency) == tuple and adjacency[0] == label:
					return adjacency[1]
			return None

	def show(self):
		if self.root:
			self.show_recursively(self.root, [], 0)

	def partial_match(self, to_match):
		for to_match_node in [get_node_without_var(n) for n in to_match.get_nodes()]:
			if to_match_node not in [get_node_without_var(n).replace(" ", "") for n in self.get_nodes()]:
				return False
			else:
				if not included_adjacency(to_match.adjacents(to_match_node), self.adjacents(to_match_node)):
					return False
		
		return True

			
	def show_recursively(self, node, visited, level, lable=''):
		if len(lable) > 0: 
			lable += ' '
		print(' ' * level * 2 + lable + node.split("|terminal|")[0])
		if node not in visited:
			visited.append(node)
			for adjacency in self.nodes[node]:
				adjacent_node = None
				label = None
				if type(adjacency) == tuple:
					label, adjacent_node = adjacency
				else:
					adjacent_node = adjacency
				visited = self.show_recursively(adjacent_node, visited, level + 1, label)
		return visited

	def change_root(self, new_root):

		for node in self.nodes.keys():
			try:
				if node == new_root or new_root == get_node_without_var(dic_value):
					self.root = node
					return
			except Exception:
				pass

def search_ingnoring_vars(dic, node):
	node = get_node_without_var(node)
	for dic_value in dic:
		try:
			if node == get_node_without_var(dic_value):
				return dic[dic_value]
		except Exception:
			pass

def get_value(value):
	return value.split('|terminal|')[0]

def get_node_without_var(node):
	try:
		return node.split(' / ')[1].replace(" ", "")
	except:
		return node

def normalize_adjacency(the_list):
	new_list = []
	for elem in the_list:
		new_list.append((elem[0],get_node_without_var(get_value(elem[1]))))
	return new_list

def included_adjacency(listA, listB):
	listA = normalize_adjacency(listA)
	listB = normalize_adjacency(listB)
	for elementA in listA:
		if not elementA in listB:
			return False
	return True

