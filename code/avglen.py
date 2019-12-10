import numpy as np
import sys

def avglenofword(inputfile,index):
	total = 0
	numofwords = 0
	with open(inputfile, "r",encoding="utf8") as fd:
		for line in fd:
			#print(line)
			for word in line.split():
				#print(word)
				total+=len(word)
				numofwords+=1

	print("average length of characters per concept for document" +  str(index) +  "  " + str(total/numofwords))

def avglenofsentence(inputfile,index):
	total = 0
	numofsentences = 0
	with open(inputfile, "r",encoding="utf8") as fd:
		for line in fd:
			numofsentences+=1
			for word in line.split():
				#print(word)
				total+=1

	print("average length of sentence for document" + str(index) +  "  " + str(total/numofsentences))



def main():
	
	"""avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt",1)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/2.txt",2)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/3.txt",3)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/4.txt",4)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/5.txt",5)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/6.txt",6)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/7.txt",7)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/8.txt",8)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/9.txt",9)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/10.txt",10)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/11.txt",11)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/12.txt",12)
	avglenofword("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/13.txt",13)
	"""
	"""
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt",1)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/2.txt",2)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/3.txt",3)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/4.txt",4)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/5.txt",5)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/6.txt",6)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/7.txt",7)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/8.txt",8)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/9.txt",9)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/10.txt",10)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/11.txt",11)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/12.txt",12)
	avglenofsentence("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/13.txt",13)
	"""
	avglenofword(sys.argv[1],sys.argv[2])
	avglenofsentence(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
	main()