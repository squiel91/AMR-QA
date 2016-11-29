import graph
import AMR
import xml.etree.ElementTree as ET

tree = ET.parse('amr-bank-v1.6.xml')
root = tree.getroot()
AMR_forest = []
for xml_sentence_amr in root:
 	try:
 		amr_sentence = xml_sentence_amr.getchildren()[1].text
 		amr_sentence = " ".join(filter(
 			lambda x: len(x) > 0, 
 			amr_sentence.replace("\n", " ").split(" "))
 		)
 		AMR_forest.append(AMR.to_graph(amr_sentence))
 	except Exception:
 		print("Could not process: " + amr_sentence)

# finally! do something interesitng with AMR_forest.