#!/usr/bin/env python3
import string
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import os


def plot(word_freq, title):
    word_freq = sorted(word_freq.values(), reverse=True)
    word_freq_sum = np.sum(word_freq)
    word_freq_prob = [e / word_freq_sum for e in word_freq]
    # word_freq_prob = word_freq
    log_word_freq = [math.log(e) for e in word_freq_prob]
    n = len(word_freq)

    ranks = [i + 1 for i in range(n)]
    log_ranks = [math.log(i + 1) for i in range(n)]

    pareto_x = ranks
    pareto_fit_beta = np.min(pareto_x)
    pareto_fit_alpha = n * 1.0 / \
                       (np.sum([math.log(pareto_x[i])
                                for i in range(n)]) - n * math.log(pareto_fit_beta))

    pareto = [pareto_fit_alpha *
              (pareto_fit_beta ** pareto_fit_alpha) /
              pareto_x[i] ** (pareto_fit_alpha + 1)
              for i in range(n)]

    log_pareto = [math.log(e) for e in pareto]

    ols_beta = 1 / np.dot(np.array(log_ranks), np.array(log_ranks)) * np.dot(np.array(log_ranks),
                                                                             np.array(log_word_freq))

    # print('Plottig {t}_xsong1.pdf...'.format(t=title))
    plt.figure()
    plt.scatter(log_ranks, log_word_freq, c='red', label='original')
    porato_label = 'Pareto (alpha={a} beta={b})'.format(
        a=round(pareto_fit_alpha, 4), b=round(pareto_fit_beta, 3))
    plt.scatter(log_ranks, log_pareto, c='green', label=porato_label)
    print(porato_label)
    # plt.scatter(log_ranks, np.multiply(ols_beta, log_ranks), c='blue',
    #             label='OLS (beta={b})'.format(b=round(ols_beta, 3)))
    plt.title(title)
    plt.legend()
    plt.ylabel('Word frequency in log scale')
    plt.xlabel('Rank in log scale')
    # plt.savefig('{t}_xsong1.pdf'.format(t=title))  # actual output
    plt.savefig('{t}.png'.format(t=title))  # smaller images for latex
    plt.close()


def get_stats_plot(input_path):
    with open(input_path, 'r') as f:
        words = f.read().strip().lower().translate(
            str.maketrans('', '', string.punctuation)).split()
        # punctuation, lower
        unigrams = {}
        bigrams = {}
        trigrams = {}

        for i in range(len(words)):
            # unigrams
            unigram = words[i]
            unigrams[unigram] = unigrams.get(unigram, 0) + 1

            # bigrams
            if i >= 1:
                bigram = " ".join([words[i - j] for j in range(1, -1, -1)])
                bigrams[bigram] = bigrams.get(bigram, 0) + 1

            # trigrams
            if i >= 2:
                trigram = " ".join([words[i - j] for j in range(2, -1, -1)])
                trigrams[trigram] = trigrams.get(trigram, 0) + 1


        print('Unigrams')
        filename = os.path.splitext(os.path.basename(input_path))[0]
        plot(unigrams, f'{filename}_Unigram')
        print('Bigrams')
        plot(bigrams, f'{filename}_Bigrams')
        print('Trigrams')
        plot(trigrams, f'{filename}_Trigrams')


def main():
    input_path = 'data/original'
    for file in os.listdir(input_path):
        text_file = f'{input_path}/{file}'
        print(text_file)
        get_stats_plot(text_file)
        print()


if __name__ == '__main__':
    main()
