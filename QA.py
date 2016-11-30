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
Luis Chiruzzo (@luischiruzzo), Ezequiel Santiago Sanchez (@squiel91)
2016, Universidad de la Republica, Montevideo, Uruguay
------------------------------------------------------------------''')

while True:
	inquire = input("\n> Enter a question (between quotes!): ")
	print("\nProcessing, sorry about that.\n---------------\n\n")
	inquire_graph = AMR.parse(inquire)
	print("---------------\n\nDone Processing!\n")
	respond = ask_me.answer(inquire_graph)
	print("Answer: \n{}".format(respond))


