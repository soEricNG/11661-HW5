import sys
import nltk

def TTRatio(inputfile,index):
	lines = []
	unigramwordcount = {}
	count = 0
	with open(inputfile, "r",encoding="utf8") as fd:
		for line in fd:
			lines.append(line)
			for word in line.split():
				print(word)
				count+=1
				if word not in unigramwordcount:
					unigramwordcount[word]=1
				else:
					unigramwordcount[word]+=1

	print(count)
	typecount = len(unigramwordcount.keys())
	tokencount = sum(unigramwordcount.values())
	print(tokencount)

	TTR = typecount/tokencount
	print("TTR for Document " + str(index) + ": " + str(TTR))


def main():
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt",1)
	"""
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt",1)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/2.txt",2)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/3.txt",3)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/4.txt",4)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/5.txt",5)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/6.txt",6)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/7.txt",7)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/8.txt",8)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/9.txt",9)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/10.txt",10)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/11.txt",11)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/12.txt",12)
	TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/13.txt",13)
	"""
	#TTRatio("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/13.txt",13)
	
if __name__ == "__main__":
	main()

