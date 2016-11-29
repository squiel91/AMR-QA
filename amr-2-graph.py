import re
import pdb
import graph

# still need to add reentrancy

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

def amr_2_graph(sentence, graph):
	# pdb.set_trace()
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

sentence = '(s / see-01 :ARG0 (i / i) :ARG1 (p / picture :mod (m / magnificent) :location (b2 / book :wiki - :name (n / name :op1 "True" :op2 "Stories" :op3 "from" :op4 "Nature") :topic (f / forest :mod (p2 / primeval)))) :mod (o / once) :time (a / age-01 :ARG1 i :ARG2 (t / temporal-quantity :quant 6 :unit (y / year))))'
# sentence = '(p / ponder-01 :ARG0 (i / i) :ARG1 (a / adventure :location (j / jungle)) :ARG1-of (d / deep-02) :time (t / then))'
sentence = '(a / add-01 :ARG0 (s / she) :ARG1 (t / think-01 :ARG0 s :ARG1 (t2 / time :purpose (b / breakfast-01))) :time (l / late :degree (m / more :quant (i / instant))))'
print("")
# sentence = '(b2 / book :name (n / name :op1 "True" :op2 "Stories" :op3 "from" :op4 "Nature") :topic (f / forest :mod (p2 / primeval)))'
print(sentence)

sentence = sentence.replace(":wiki - ", "")

g = graph.Graph()
amr_2_graph(sentence, g)
g.show()

