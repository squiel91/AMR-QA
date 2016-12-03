import little_prince_corpus
import graph as g
from answer import Answer
import AMR

# Parse module
little_prince, originals = little_prince_corpus.AMR_graphs('amr-bank-v1.6.xml')
ask_me = Answer(little_prince, originals)

print(
'''
QUESTION & ANSWERING to Little Prince using AMR
------------------------------------------------------------------
Luis Chiruzzo (@luischiruzzo), Ezequiel Santiago Sanchez (@squiel91)
2016, Universidad de la Republica, Montevideo, Uruguay
------------------------------------------------------------------''')

while True:
	inquire = input("\n> Enter a question (between quotes!): ")
	inquire = inquire.lower()
	print("\nProcessing.\n---------------")
	inquire_graph = AMR.parse(inquire)
	print("---------------\nDone Processing!\n")
	respond = ask_me.answer(inquire_graph, inquire)


