#!/usr/bin/env python3

import os
import time
import sys
import string



# load file
def load_file():
    filename = sys.argv[-2]
    with open(filename, 'r') as f:
        string_of_lines = ''
        for line in f:
            translator = str.maketrans("", "", string.punctuation)
            # remove punctuation and whitespace, make lowercase
            clean_line = line.translate(translator).replace('\n', ' ').lower()
            string_of_lines += clean_line
        # each word in the text is split into elements of a list
        result = string_of_lines.split()
        return result

# at the command line prompt user to enter word pair e.g. 'cat hat'.
# Press enter to move to newline. Press enter twice to exit.
def word_pair():
    pair_of_words = []
    while True:
        line = input()
        if line:
            pair_of_words.append(line.split())
        else:
            break
    return pair_of_words


# calculate the word cooccurrence probability
def co_occur(sentence):
    word_pairs = word_pair()
    index_word_pair = 0
    for sublist in word_pairs:
        wordA = word_pairs[index_word_pair][0]
        wordB = word_pairs[index_word_pair][1]
        index_word_pair += 1

        # when wordA is not found in the text, output 0.00
        if wordA not in sentence:
            print('0.00')
            # before it tries to divide 0 by 0
            break

        # count the number of times wordA appears in sentence (denominator)
        count_wordA = 0
        for word in sentence:
            if word == wordA:
                count_wordA += 1

        # get the index of anywhere wordA appears in sentence
        # if the word is not in the sentence an empty list is returned.
        result = [index for index, element in enumerate(sentence) if element == wordA]

        # search for wordB within range, k of wordA 
        try:
            # count the number of times wordB appears around wordA (numerator)
            count_wordB = 0
            for i in result:
                global count_wordB
                k = int(sys.argv[-1])
                increment = 1
                while increment <= k:
                    if k + 1 < len(sentence) - 1 and not i+increment > len(sentence) - 1:
                        if sentence[i+increment] == wordB:
                            count_wordB += 1
                            break
                    if k - 1 >= 0 and not i-increment < 0:
                        if sentence[i-increment] == wordB:
                            count_wordB += 1
                            break
                    increment += 1
        except IndexError:
            pass

        print('%.2f' % (count_wordB / count_wordA))



if __name__ == '__main__':
    sentence = load_file()
    co_occur(sentence)
