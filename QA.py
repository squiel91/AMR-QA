import little_prince_corpus
import graph as g
from answer import Answer
import AMR

# Parse module
little_prince = little_prince_corpus.AMR_graphs('amr-bank-v1.6.xml')
ask_me = Answer(little_prince)

print(
'''
QUESTION & ANSWERING to Little Prince using AMR
------------------------------------------------------------------
Luis Chiruzzo (@luischir), Ezequiel Santiago Sanchez (@squiel91)
2016, Universidad de la República, Montevideo, Uruguay
------------------------------------------------------------------
''')
while True:
	inquire = input("Enter a question or fact: ")
	print(inquire)
	inquire_graph = AMR.parse(inquire)
	respond = ask_me.answer(inquire_graph)
	print("Answer: \n{}".format(respond))


