import sys
import numpy as np
import collections
import nltk


def createdata(inputfile):
    lines = []

    with open(inputfile, "r",encoding="utf8") as fd:
        for line in fd:
            lines.append(line.split("\n")[0])

    trainingdata = lines[:-50]
    testdata = lines[-50:]

    return trainingdata,testdata

def uniperplexity(trainingdata):
    unigramwordcount = collections.defaultdict(lambda: 0.01)

    for line in trainingdata:
        for word in line.split():
            if word not in unigramwordcount:
                unigramwordcount[word]=1
            else:
                unigramwordcount[word]+=1
    
    N = float(sum(unigramwordcount.values()))
    for word in unigramwordcount:
        unigramwordcount[word] = unigramwordcount[word]/N

    return unigramwordcount

def perplexitycalculation(testset,model):
    testset = testset.split()
    perplexity = 1
    N = 0
    for word in testset:
        N += 1
        perplexity = perplexity * (1/model[word])
    perplexity = pow(perplexity, 1/float(N)) 
    return perplexity

def main():
    inputfile = "F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt"
    trainingdata, testdata = createdata(inputfile)
    model = uniperplexity(trainingdata)
    sum_p = 0
    for i in testdata:
        print(i)
        k = perplexitycalculation(i,model)
        sum_p += k
    print("Average Perplexity " + str(sum_p/len(testdata)))


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    uniperplexity("F:/CMU Courses/11661 Language and Statistics/Assignment 5/data/1.txt")