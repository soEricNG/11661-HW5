import regex as re
import sys
import math
#from prettytable import PrettyTable
import random

unigram_frequency = {}
bigram_frequency = {}
total = 0
unigram_probabilities = {}
bigram_probabilities = {}

def tokenize(text):
	#text = re.sub(r'\n', "", text)
	#print(text)
	#sentences = re.findall(r'[A-ZÅÄÖ].+?\.', text)
	sentences = text.split("\n")
	#print(sentences)
	#sentences = list(map(lambda s: s.lower(), sentences))
	#sentences = list(map(lambda s: re.sub(r'[\-,;:!?.’\'«»()–...&‘’“”*—]', "", s), sentences))
	sentences = list(map(lambda s: '<s> ' + s + ' </s>', sentences))
	text = " ".join(sentences)
	#print(text)
	return text

def train(text):
	#print(text)
	text = tokenize(text)
	wordlist = []
	global total

	# Unigram calculations
	words = text.split()
	#print(words)
	total = len(words)
	for word in words:
		if word in unigram_frequency:
			unigram_frequency[word] += 1
		else:
			wordlist.append(word)
			unigram_frequency[word] = 1
	for word in unigram_frequency:
		unigram_probabilities[word] = unigram_frequency[word]/total

	#print(unigram_probabilities['ЁϨϱ'])

	# Bigram calculations
	bigrams = [tuple(words[inx:inx + 2])
				for inx in range(len(words) - 1)]
	for bigram in bigrams:
		if bigram in bigram_frequency:
			bigram_frequency[bigram] += 1
		else:
			bigram_frequency[bigram] = 1
	for bigram in bigram_frequency:
		bigram_probabilities[bigram] = bigram_frequency[bigram]/unigram_frequency[bigram[0]]
	return wordlist

def unigram_sentence_probability(sentence):
	#sentence = re.sub(r'\n', "", sentence)
	#sentence = sentence.lower()
	#sentence = re.sub(r'[\-,;:!?.’\'«»()–...&‘’“”*—]', "", sentence)
	sentence = sentence + ' </s>'
	words = sentence.split()
	#print(words)

	#print("----------Unigram probability----------")

	probability = 1
	entropy = 0
	table = PrettyTable(["wi", "C(wi)", "#words", "P(wi)"])
	for word in words:
		probability = probability*unigram_probabilities[word]
		entropy += math.log2(unigram_probabilities[word])

	#print(table)
	
	#print("=========================================")
	#print("Sentence probability: " + str(probability))

	entropy = -1/len(words)*entropy
	#print("Entropy rate: " + str(entropy))

	perplexity = math.pow(2,entropy)
	#print("Perplexity: " + str(perplexity))
	#print("")
	return perplexity

def bigram_sentence_probability(sentence):
	#sentence = re.sub(r'\n', "", sentence)
	#sentence = sentence.lower()
	#sentence = re.sub(r'[\-,;:!?.’\'«»()–...&‘’“”*—]', "", sentence)
	sentence = '<s> ' + sentence + ' </s>'
	words = sentence.split()
	bigrams = [tuple(words[inx:inx + 2])
				for inx in range(len(words) - 1)]


	#print("----------Bigram probability----------")

	probability = 1
	entropy = 0
	table = PrettyTable(["wi wi+1", "Ci,i+1", "C(i)", "P(wi+1|wi)", "backoff"])
	for bigram in bigrams:
		bigram_str = str(bigram[0]) + " " + str(bigram[1])
		prob = 0
		freq = 0
		backoff = ""
		if bigram in bigram_probabilities:
			freq = bigram_frequency[bigram]
			prob = bigram_probabilities[bigram]
		else:
			backoff = bigram[1]
			freq = 0
			prob = unigram_probabilities[bigram[1]]

		table.add_row([
			bigram_str, 
			str(freq),
			str(unigram_frequency[bigram[0]]),
			str(prob),
			backoff
		])

		probability = probability*prob
		entropy += math.log2(prob)

	#print(table)
	
	#print("=========================================")
	#print("Sentence probability: " + str(probability))

	entropy = -1/len(bigrams)*entropy
	#print("Entropy rate: " + str(entropy))
	perplexity = math.pow(2,entropy)
	#print("Perplexity: " + str(perplexity))
	return perplexity

def sentence_probability(sentence, probabilities):
	words = re.split(r'\s',sentence)
	#print(words)
	probability = 1
	for word in words:
		probability = probability*probabilities[word]
	return probability

def generate_random_data(wordlist):
	testdata = []
	num_of_sentences = 5
	num_of_words = 5
	text  = ""
	for m in range(num_of_sentences):
		text = ""
		for i in range(0,num_of_words):
			k = random.randint(0,len(wordlist))
			text += wordlist[k] + " "
		testdata.append(text)
	#print(testdata)
	return testdata


def processdata(inputfile):
	text = ""
	totaldata = []
	testdata = []
	with open(inputfile,encoding="utf8") as fd:
		for line in fd:
			line = line.split("\n")[0]
			totaldata.append(line)
			#text += line
	#text = "ϽϪϲ ϲ ϰ ϫϱ ϸϲ ϭϩ ϲ ϰ ϱϭ ϲϪϽ ϸϱϴ ϰϮϴ ϱϺϨ Ѐϭ \n ϮЂ ϰЀ ϾϪϹϱ Ϯ ϰϱϲϱ ϫϲϮϮϨ Ϯ ϼЀ ϭϫϺ"
	traindata = " ".join(totaldata)
	#print (traindata)
	#print(traindata)
	testdata = totaldata[-50:]
	#print(testdata)
	#print(testdata)
	wordlist = train(traindata)
	#print(wordlist)
	#testdata = generate_random_data(wordlist)
	for i in testdata:
		i = i.rstrip()
		i = i.lstrip()
		if i=='':
			testdata.remove('')

	#print(testdata)
	ratio = 0
	for i in testdata:
		#i = i.split("\n")[0]
		#print(i)
		i = i.rstrip()
		i = i.lstrip()
		#print(i)
		uniperplexity = unigram_sentence_probability(i)
		biperplexity = bigram_sentence_probability(i)
		ratio+=(uniperplexity/biperplexity)

	print(ratio/len(testdata))

if __name__ == '__main__':
	processdata(sys.argv[1])
	"""
	processdata("1.txt")
	processdata("2.txt")
	processdata("3.txt")
	processdata("4.txt")
	processdata("5.txt")
	processdata("6.txt")
	processdata("7.txt")
	processdata("8.txt")
	processdata("9.txt")
	processdata("10.txt")
	processdata("11.txt")
	processdata("12.txt")
	processdata("13.txt")
	"""