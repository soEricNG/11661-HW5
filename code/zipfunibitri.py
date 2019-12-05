
from paretochart import pareto
import csv
from nltk.util import ngrams
import operator
from collections import Counter
from matplotlib import pyplot as plt
import sys


def zipfgraph(inputfile,index):
    unigramwordcount = {}
    bigramwordcount = {}
    trigramwordcount = {}
    lines = []

    #creating a dictionary for unigrams
    with open(inputfile, "r",encoding="utf8") as fd:
        for line in fd:
            lines.append(line)
            for word in line.split():
                if word not in unigramwordcount:
                    unigramwordcount[word]=1
                else:
                    unigramwordcount[word]+=1
                    

    sortedunigramwordcount = sorted(unigramwordcount.items(), key = lambda x: x[1],reverse=True)

    #creating a dictionary for bigrams
    bi_gram = 2
    text = "".join(lines)
    bigram = Counter(ngrams(text.split(),bi_gram),reverse=True)
    for words,value in bigram.most_common(10):
        if words not in bigramwordcount:
            bigramwordcount[words] = value
        else:
            bigramwordcount[words]+=1
            

    #creating a dictionary for trigrams
    tri_gram = 3
    trigram = Counter(ngrams(text.split(),tri_gram),reverse=True)
    for words,value in trigram.most_common(10):
        if words not in trigramwordcount:
            trigramwordcount[words] = value
        else:
            trigramwordcount[words]+=1
            

    unigramgraph = []
    for i in sortedunigramwordcount:
        unigramgraph.append(i[1])
        
    bigramgraph = []

    for i in bigramwordcount:
        bigramgraph.append(bigramwordcount[i])
        
    trigramgraph = []
    for i in trigramwordcount:
        trigramgraph.append(trigramwordcount[i])
        

    #plotting the zipf's law plot in loglog scale for unigrams
    plt.loglog(unigramgraph)
    plt.title("Zipf Law (Unigram) for document " + str(index))
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.show()

    #plotting the zipf's law plot in loglog scale for bigrams
    plt.loglog(bigramgraph)
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Zipf Law (Bigram) for document " + str(index))
    plt.show()

    #plotting the zipf's law plot in loglog scale for trigrams
    plt.loglog(trigramgraph)
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Zipf Law (Trigram) for document " + str(index))
    plt.show()

    #pareto(unigramgraph[0:10])
    #plt.title('Pareto Plot', fontsize=10)
    #plt.show()

def main():
    #zipfgraph("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt",1)
    zipfgraph(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()

