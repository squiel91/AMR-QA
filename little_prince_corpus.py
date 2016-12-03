import graph
import AMR
import xml.etree.ElementTree as ET

def AMR_graphs(xml_corpus):
	tree = ET.parse(xml_corpus)
	root = tree.getroot()
	AMR_forest = []
	AMR_originals = []
	for xml_sentence_amr in root:
	 	try:
	 		amr_original = xml_sentence_amr.getchildren()[0].text
	 		amr_sentence = xml_sentence_amr.getchildren()[1].text
	 		amr_sentence = " ".join(filter(
	 			lambda x: x, 
	 			amr_sentence.replace("\n", " ").split(" "))
	 		)
	 		AMR_forest.append(AMR.to_graph(amr_sentence))
	 		AMR_originals.append(amr_original)
	 	except Exception:
	 		print("Could not process: " + amr_sentence)

	# finally! do something interesitng with AMR_forest.
	return AMR_forest, AMR_originals