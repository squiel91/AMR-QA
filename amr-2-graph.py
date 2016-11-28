import pdb

def find_argument(sentence, initial=0):
	pos = sentence[initial:].find(':')
	if pos >= 0:
		return sentence[initial:].find(':') + initial
	else: 
		return -1

def find_closing_parentheis(sentence, initial=0):
	number_still_opened_parenthesis = 0
	if  sentence[initial] != '(':
		raise Exception("Error: Initial character should be an opening parenthesis.")

	for pos in range(initial, len(sentence) + 1):
		if sentence[pos] == '(':
			number_still_opened_parenthesis += 1
		if sentence[pos] == ')':
			number_still_opened_parenthesis -= 1
			if number_still_opened_parenthesis == 0:
				return pos
	raise Exception("Error: Not balanced parenthesis.")

def amr_2_graph(sentence, initial=0):
	if  sentence[initial] != '(':
		raise Exception("Error: Initial character should be an opening parenthesis.")
	else:
		initial += 1
	if  sentence[-1] != ')':
		raise Exception("Error: Last character should be a closing parenthesis.")
	root_start = initial
	root_end = min(sentence[initial:].find(':'), sentence[initial:].find('('), sentence[initial:].find(')'))
	root = sentence[root_start:root_end]
	print(root)
	actual = root_end + 1
	# pdb.set_trace()
	while find_argument(sentence, initial=actual) >= 0:
		argument_start_flag_index = find_argument(sentence, initial=actual)
		argument_end_flag_index = sentence[argument_start_flag_index:].find(" ") + argument_start_flag_index
		argument = sentence[argument_start_flag_index:argument_end_flag_index]
		print(argument)
		actual=argument_end_flag_index+1
		if sentence[actual] != '(':
			actual_old = actual
			actual += sentence[actual:].find("(")
			print("Warning: characters omited {}".format(sentence[actual_old:actual]))
		
		end_subgraph_flag = find_closing_parentheis(sentence, initial=actual) + 1
		subgraph = sentence[actual: end_subgraph_flag]
		print(subgraph)
		amr_2_graph(subgraph)
		actual = end_subgraph_flag
		# pdb.set_trace()
	return sentence[root_start:root_end]


sentence = '(s / see-01 :ARG0 (i / i) :ARG1 (p / picture :mod (m / magnificent) :location (b2 / book :wiki - :name (n / name :op1 "True" :op2 "Stories" :op3 "from" :op4 "Nature") :topic (f / forest :mod (p2 / primeval)))) :mod (o / once) :time (a / age-01 :ARG1 i :ARG2 (t / temporal-quantity :quant 6 :unit (y / year))))'
sentence = '(b2 / book :wiki - :name (n / name :op1 "True" :op2 "Stories" :op3 "from" :op4 "Nature") :topic (f / forest :mod (p2 / primeval)))'
sentence = '(p / ponder-01 :ARG0 (i / i) :ARG1 (a / adventure :location (j / jungle)) :ARG1-of (d / deep-02) :time (t / then))'

if type(sentence) is not str:
	raise Exception("Error: Not a string.")
# print(find_closing_parentheis("(hello(world)yeah)gdfg"))
# pdb.set_trace()
print(amr_2_graph(sentence))

