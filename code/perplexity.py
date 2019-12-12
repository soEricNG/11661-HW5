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

unigram_count = {}
bigram_count = {}
trigram_count = {}
total_occurrences = 0


def process(filename, threshold=1):
    """
    1. Concatenate all lines to a single line
    2. Add space before all punctuation
    3. Replace white space with single space
    4. Replace infrequent word with a symbol
    :param threshold: threshold for infrequent word
    :param filename: file path
    :return: a single line
    """
    with open(filename, 'r') as f:
        single_line = " ".join(line.strip() for line in f)
        # Which one to use for punctuation?
        # lower perplexity is better
        # single_line = re.sub(r'([^\w^s])', r' \1 ', single_line)
        single_line = re.sub('([.,!?()\'/])', r' \1 ', single_line)
        single_line = re.sub('\s{2,}', ' ', single_line)

        vocabulary = {}
        words = single_line.split(" ")
        for token in words:
            vocabulary[token] = vocabulary.get(token, 0) + 1
        infrequent_list = [key for key, value in vocabulary.items() if value < threshold]
        for i in range(len(words)):
            if words[i] in infrequent_list:
                words[i] = 'UNKNOWN_WORD'
        return " ".join(words)


def get_ngram_count(single_line, n):
    """
    Calculate the ngram count in the single line string
    :param n: 1 or 2 or 3
    :param single_line: result from preprocessing the train file
    :return: a dictionary that stores the frequency counts of ngrams
    """
    # do some corner case when current index is less than n. Should I do this or not?
    ngram_count = {}
    words = single_line.split(" ")
    for i in range(n - 1, len(words)):
        token = " ".join([words[i - j] for j in range(n - 1, -1, -1)])
        ngram_count[token] = ngram_count.get(token, 0) + 1
    return ngram_count


def print_ngram_descending(ngram_count):
    """
    Print the dictionary in descending order
    :param ngram_count:
    :return:
    """
    return sorted(ngram_count.items(), key=lambda kv: kv[1], reverse=True)


def get_prob(word, model, history):
    """
    Get the probability of the word based on the model
    :param word: the word
    :param history: list words in history ,[] in uniform model
    :param model: 0 for uniform, 1 for unigram, 2 for bigram, 3 for trigram
    :return: the probability in float
    """
    global unigram_count
    global total_occurrences
    global bigram_count
    global trigram_count
    if model == 0:
        return 1.0 / len(unigram_count)
    elif model == 1:
        unigram = word
        if unigram in unigram_count:
            return unigram_count[unigram] * 1.0 / total_occurrences
        return 1.0 / len(unigram_count)
    elif model == 2:
        if len(history) == 1:
            unigram = " ".join(history)
            bigram = unigram + " " + word
            if bigram in bigram_count:
                return bigram_count[bigram] * 1.0 / unigram_count[unigram]
        return 1.0 / len(unigram_count)
    elif model == 3:
        if len(history) == 2:
            bigram = " ".join(history)
            trigram = bigram + " " + word
            if trigram in trigram_count:
                return trigram_count[trigram] * 1.0 / bigram_count[bigram]
        return 1.0 / len(unigram_count)
    else:
        raise Exception('Model should be one of 0, 1, 2, 3')


def get_perplexity_by_word(word, history, model):
    """
    Calculate perplexity of a word based on interpolation
    :param word: single word
    :param history: list of words before it capped at 2
    :return: the perplexity in float
    """
    model_history = [] if model < 1 else history[:model - 1]
    prob = get_prob(word, model, model_history)
    # print(str(model) + ":" + str(prob))
    return math.log(prob)


def get_perplexity(single_line, n):
    """
    Calculate perplexity based on interpolation
    :param single_line: result from preprocessing the test file
    :return: the perplexity in float
    """
    words = single_line.split(" ")
    res = 0.0
    history = []
    for i in range(len(words)):
        # Add previous word to history
        if i > 0:
            history.append(words[i - 1])
        # Remove word that is more than 2 apart
        if i > 2:
            history = history[1:]
        # print(history)
        res += get_perplexity_by_word(words[i], history, n)
    # Normalize by sequence size
    return math.exp(-res / len(words))


def output(perplexity, output_path):
    """
    Output the perplexity to the output path
    :param perplexity: perplexity in float
    :param output_path: output path
    :return: void
    """
    with open(output_path, 'a') as f_out:
        f_out.write('%.2f\n' % perplexity)


def process_test(filename, vocabulary):
    with open(filename, 'r') as f:
        single_line = " ".join(line.strip() for line in f)
        # Which one to use for punctuation?
        # lower perplexity is better
        # single_line = re.sub(r'([^\w^s])', r' \1 ', single_line)
        single_line = re.sub('([.,!?()\'/])', r' \1 ', single_line)
        single_line = re.sub('\s{2,}', ' ', single_line)

        words = single_line.split(" ")
        for i in range(len(words)):
            if words[i] not in vocabulary:
                words[i] = 'UNKNOWN_WORD'
        return " ".join(words)


def my_ngram_perplexity(train, test):
    # Preprocess train data
    # print("Start processing train text...")
    train_text = process(train)
    # print("Finished processing train text...")

    # Calculate N gram count

    global unigram_count
    global bigram_count
    global trigram_count
    global total_occurrences

    # print("Start unigram calculation...")
    unigram_count = get_ngram_count(train_text, 1)
    # print("Finished unigram calculation...")

    total_occurrences = sum(unigram_count.values())

    # print("Start bigram calculation...")
    bigram_count = get_ngram_count(train_text, 2)
    # print("Finished bigram calculation...")

    # Preprocess test data
    # print("Start processing test text...")
    test_text = process_test(test, list(unigram_count.keys()))
    # print("Finished processing test text...")

    # Calculate perplexity
    # print("Start calculating perplexity...")
    unigram_result = get_perplexity(test_text, 1)
    bigram_result = get_perplexity(test_text, 2)
    # print("Finished calculating perplexity...")

    # Output
    # print("Output...")
    print(f'unigram: {unigram_result}')
    print(f'bigram: {bigram_result}')


def ngrams_pad(sent, n):
    if n == 1:
        return ngrams(sent, 1)
    elif n > 1:
        return ngrams(sent, n, pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>")


def nltk_ngram_perplexity(train, test):
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
        print(f'unigram: {model.perplexity(test_d)}')
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
        print(f'bigram: {model.perplexity(test_d)}')
        # print(model.entropy(test_d))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate perplexity')
    parser.add_argument('--train', type=str, required=True, help='train file name')
    parser.add_argument('--test', type=str, required=True, help='test file name')
    args = parser.parse_args()
    print('NLTK VERSION:')
    nltk_ngram_perplexity(args.train, args.test)
    print('MY VERSION:')
    my_ngram_perplexity(args.train, args.test)
