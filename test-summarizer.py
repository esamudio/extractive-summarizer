#!/usr/bin/env python3

import argparse
from utils import load_file, summarizer

# constants
TOLERANCE = 0.00001
THRESHOLD = 0.1
DESC = '''This application summarizes a given article using previously calculated inverse document frequencies (idf).'''
IDF_FILE_DESC = '''File containing idf values of words seen in training.'''
ORIGINAL_FILE_DESC = '''File to summarize.'''


if __name__ == '__main__':
    # setup argument parser
    parser = argparse.ArgumentParser(prog='test-summarizer', description=DESC)
    parser.add_argument('IDF_FILE', type=str, help=IDF_FILE_DESC)
    parser.add_argument('ORIGINAL_FILE', type=str, help=ORIGINAL_FILE_DESC)
    args = parser.parse_args()

    # compute summary
    words_idf = load_file(args.IDF_FILE)
    summary = summarizer(args.ORIGINAL_FILE, THRESHOLD, words_idf, TOLERANCE)

    # output summary
    with open(args.ORIGINAL_FILE + '.summary', 'w') as outfile:
        outfile.write(summary)
