import os
# Note that camr AMR parser (https://github.com/c-amr/camr) should be installed

def generate_file(content, name, directory=""):
	if dir:
		name = directory + "/" + name
	file = open(name, 'w')
	file.write(content)
	file.close()
	return file

def get_content_file(name, directory=""):
	if dir:
		name = directory + "/" + name
	file = open(name, 'r')
	return file.read()

def run_command(command):
	os.system(command)

model_file = 'LDC2014T12.m'

def parse(sentence):
	run_command("cd camr\nfind . -name 'input_sentence_file*' -exec rm \{\} \;")
	input_sentence_file = "input_sentence_file.txt"
	generate_file(sentence, input_sentence_file, "camr")
	run_command("cd camr\npython amr_parsing.py -m preprocess {}".format(input_sentence_file))
	run_command("cd camr\npython amr_parsing.py -m parse --model {} {}".format(model_file, input_sentence_file))
	parsed_visual_txt = get_content_file(input_sentence_file + ".all.LDC2014T12.parsed", "camr")
	removed_headers = " ".join(parsed_visual_txt.replace("\t", " ").split("\n")[2:])
	parsed_txt = " ".join(filter(lambda x: len(x) > 0, removed_headers.split(" ")))
	return parsed_txt
