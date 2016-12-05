from pdb import set_trace as st

qw = [
	('for who', [':ARG2']),
	('how long', [':duration']),
	('from where', [':origin']),
	('to where', [':destination']),
	('who', [':ARG0']),
	('what', [':topic', ':ARG1']),
	('when', [':time']),
	('where', [':location']),
	('how', [':manner', ':instrument', ':mode']),
	('why', [':purpose']),
]

def relation_to_look_for(sentence, q):
	for question_word, relations in q:
		if question_word in sentence:
			return relations, question_word
	return None

class Answer:
	def __init__(self, corpus, originals):
		self.corpus = corpus
		self.originals = originals


	def answer(self, question_AMR_graph, inquire):
		relationship = relation_to_look_for(inquire, qw)
		check_fact = False
		relations_inquired, word = (None, None)
		if relationship:
			relations_inquired, word = relation_to_look_for(inquire, qw)
		else:
			check_fact = True
		print("Answer to '{}':\n".format(inquire))
		print("AMR representation:")
		question_AMR_graph.show()

		print("\n")
		if check_fact:
			word = "fact"
		print('{}:'.format(word))
		answers_quantity = 0
		phrase_index = 0
		for corpus_sent in self.corpus:
			phrase_index += 1
			if corpus_sent.partial_match(question_AMR_graph):
				if check_fact:
					print("----------------")
					corpus_sent.show() 
					print("{}: {}".format(phrase_index, self.originals[phrase_index - 1]))
					answers_quantity += 1
				else:
					for relation in relations_inquired:
						answer_tree = corpus_sent.adjacents(question_AMR_graph.root, label=relation)
						corpus_sent.change_root(answer_tree)
						if answer_tree:
							print("----------------")
							corpus_sent.show() 
							print("{}: {}".format(phrase_index, self.originals[phrase_index - 1]))
							answers_quantity += 1
						
		print("\n{} answer(s)".format(answers_quantity))
		if check_fact:
			if answers_quantity > 0:
				print("Is true")
			else:
				print("No evidence")
