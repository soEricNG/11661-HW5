import argparse
import sys
import re
import math
import nltk
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import Laplace
from nltk.util import ngrams
from nltk.lm import Vocabulary
import itertools


def ngrams_pad(sent, n):
    if n == 1:
        return ngrams(sent, 1)
    elif n > 1:
        return ngrams(sent, n, pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>")


def ngram_perplexity(train, test):
    # Unigram

    train_sentences = [line.strip() for line in open(train, 'r')]
    tokenized_text = [list(nltk.tokenize.word_tokenize(sent))
                      for sent in train_sentences]
    single_line = [list(itertools.chain.from_iterable(tokenized_text))]

    n = 1
    # train_data = [ngrams(sent, 1) for sent in tokenized_text]
    train_data = [ngrams(sent, 1) for sent in single_line]


    model = Laplace(n)
    words = [word for sent in tokenized_text for word in sent]
    padded_vocab = Vocabulary(words)
    model.fit(train_data, padded_vocab)

    test_sentences = [line.strip() for line in open(test, 'r')]
    tokenized_text = [list(nltk.tokenize.word_tokenize(sent))
                      for sent in test_sentences]
    single_line = [list(itertools.chain.from_iterable(tokenized_text))]

    # test_data = [ngrams(sent, 1) for sent in tokenized_text]
    test_data = [ngrams(sent, 1) for sent in single_line]

    for i, test_d in enumerate(test_data):
        print(model.perplexity(test_d))
        # print(model.entropy(test_d))

    # Bigram
    train_sentences = [line.strip() for line in open(train, 'r')]
    tokenized_text = [list(nltk.tokenize.word_tokenize(sent))
                      for sent in train_sentences]
    single_line = [list(itertools.chain.from_iterable(tokenized_text))]

    n = 2
    # train_data = [ngrams_pad(sent, n) for sent in tokenized_text]
    train_data = [ngrams_pad(sent, n) for sent in single_line]

    model = Laplace(n)
    words = [word for sent in tokenized_text for word in sent]
    words.extend(["<s>", "</s>"])
    padded_vocab = Vocabulary(words)
    model.fit(train_data, padded_vocab)

    test_sentences = [line.strip() for line in open(test, 'r')]
    tokenized_text = [list(nltk.tokenize.word_tokenize(sent))
                      for sent in test_sentences]
    single_line = [list(itertools.chain.from_iterable(tokenized_text))]

    # test_data = [ngrams_pad(sent, n) for sent in tokenized_text]
    test_data = [ngrams_pad(sent, n) for sent in single_line]

    for i, test_d in enumerate(test_data):
        print(model.perplexity(test_d))
        # print(model.entropy(test_d))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate perplexity')
    parser.add_argument('--train', type=str, required=True, help='train file name')
    parser.add_argument('--test', type=str, required=True, help='test file name')
    args = parser.parse_args()
    ngram_perplexity(args.train, args.test)
