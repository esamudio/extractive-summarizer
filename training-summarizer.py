#!/usr/bin/env python3

import argparse
from utils import word_counter
from math import log

# constants
DESC = '''This application calculates the inverse document frequencies (idf) of every word in the training data.'''
TRAINING_DIRECTORY_DESC = '''The directory containing text files to be used in training.'''
OUTPUT_FILE_DESC = '''File containing every word in training,
the amount of times each word was seen and its corresponding idf.'''


if __name__ == '__main__':
    # setup argument parser
    parser = argparse.ArgumentParser(prog='training-summarizer', description=DESC)
    parser.add_argument('TRAINING_DIRECTORY', type=str, help=TRAINING_DIRECTORY_DESC)
    parser.add_argument('OUTPUT_FILE', type=str, help=OUTPUT_FILE_DESC)
    args = parser.parse_args()

    word_counts, number_of_documents = word_counter(args.TRAINING_DIRECTORY)
    with open(args.OUTPUT_FILE, 'w') as outfile:
        for key in word_counts.keys():
            outfile.write(
                key + '\t' + str(word_counts[key]) + '\t' + str(log(number_of_documents/word_counts[key])) + '\n'
            )
