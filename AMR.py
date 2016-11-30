import re
import graph
import camr_interface as camr

def process_reentrancy(graph):
	for node_var in graph.get_nodes():
		if re.match("^[a-z][^ ]*$", node_var): # is variable 
			for node in graph.get_nodes():
				if re.match( "^{} / .*".format(node_var), node):
					graph.remove_node(node_var)
					graph.update_destination(node_var, node)

def find_closing_parenthesis(sentence):
	number_still_opened_parenthesis = 0
	if  sentence[0] != '(':
		raise Exception("Error: Initial character should be an opening parenthesis.")
	for pos in range(0, len(sentence) + 1):
		if sentence[pos] == '(':
			number_still_opened_parenthesis += 1
		if sentence[pos] == ')':
			number_still_opened_parenthesis -= 1
			if number_still_opened_parenthesis == 0:
				return (sentence[0:pos+1], sentence[pos+2:])
	raise Exception("Error: Not balanced parenthesis.")

def to_graph(sentence):
	sentence = sentence.replace(":wiki - ", "") # is the only exception
	g = graph.Graph()
	amr_2_graph(sentence, g)
	process_reentrancy(g)
	return g

def amr_2_graph(sentence, graph):
	if  sentence[0] != '(' or sentence[-1] != ')':
		raise Exception("Error: Initial and closing character should be parenthesis.")
	sentence = sentence[1:-1]
	
	if re.search('([^:)(]*)([:)(].*)', sentence):
		root, sentence = re.search('([^:)(]*)([:)(].*)', sentence).group(1, 2)
	else:
		root = sentence
		sentence = ""
	graph.add_node(root)
	while sentence.find(':') >= 0:
		terminal = False
		argument, sentence = re.search('(:[^ ]+) ?(.*)', sentence).group(1, 2)
		child_node = None
		if sentence[0] == '(':
			subgraph, sentence = find_closing_parenthesis(sentence)
			child_node = amr_2_graph(subgraph, graph)
		else:
			child_node, sentence = re.search('([^ ]+) ?(:.*)?', sentence).group(1, 2)
			if not sentence: sentence = ""
			terminal = True
		graph.add_edge(root, child_node, argument, terminal=terminal)
	return root

def parse(sentence):
	parsed_plain_string = camr.parse(sentence)
	return amr_2_graph(parsed_plain_string)

