import math

def Entropy(inputfile,base = 2.0):
	total = 0
	numofwords = 0
	text = ""
	with open(inputfile, "r",encoding="utf8") as fd:
		for line in fd:
			line = line.replace("\n","")
			text += line

	dct = dict.fromkeys(list(text))
	#print(dct)
	#calculate frequencies
	pkvec =  [float(text.count(c)) / len(text) for c in dct]

	#calculate Entropy
	H = -sum([pk  * math.log(pk) / math.log(base) for pk in pkvec ])
	return H

def Entropyofwords(inputfile,base = 2.0):
	total = 0
	numofwords = 0
	text = ""
	with open(inputfile, "r",encoding="utf8") as fd:
		for line in fd:
			line = line.replace("\n","")
			text += line

	#print(text)
	dict1 = {}
	#print(text)
	for i in text.split():
		if i not in dict1:
			dict1[i] = 1
		else:
			dict1[i] += 1

	total = sum(dict1.values())
	pkvec = [float(dict1[c]) / total for c in dict1]

	H = -sum([pk  * math.log(pk) / math.log(base) for pk in pkvec ])
	return H

def main():
	"""
	#print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 2/warandpeacedataset.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/2.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/3.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/4.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/5.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/6.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/7.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/8.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/9.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/10.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/11.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/12.txt"))
	print(Entropy("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/13.txt"))
	#print(Entropy(sys.argv[1]))
	"""
	print(Entropy(sys.argv[1]))
	print(Entropyofwords(sys.argv[1]))
	"""
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/2.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/3.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/4.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/5.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/6.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/7.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/8.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/9.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/10.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/11.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/12.txt"))
	print(Entropyofwords("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/13.txt"))
	"""
if __name__ == "__main__":
	main()


#print(Entropy("ŶŇŕūŶ űŶŲŰŃ ŘŧŻœ ŷŢŵĿű ľżŝŜ"))