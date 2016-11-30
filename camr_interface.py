import os
# Note that camr AMR parser (https://github.com/c-amr/camr) should be installed

def generate_file(content, name):
	file = open('workfile', 'w')
	file.write(content)
	return file

def get_content_file(name):
	file = open(name, 'r')
	return file.read()

def run_command(command):
	os.system(command)

model_file = 'LDC2014T12'

def parse(sentence):
	input_sentence_file = "input_sentence_file.txt"
	generate_file(sentence, input_sentence_file)
	run_command("python amr_parsing.py -m preprocess {}".format(input_sentence_file))
	run_command("python amr_parsing.py -m parse --model {model_file} {input_sentence_file} 2>log/error.log".format(model_file, input_sentence_file))
	return get_content_file(input_sentence_file + ".parsed")