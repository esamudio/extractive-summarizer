#!/usr/bin/env python3

import argparse
from utils import extract_text

# constants
DESC = '''This application evaluates our LexRank summarizer using the sentence labels provided in the dataset.'''
SUMMARIZED_FILE_DESC = '''Summarized file.'''
ORIGINAL_FILE_DESC = '''File from dataset.'''

if __name__ == '__main__':
    # setup argument parser
    parser = argparse.ArgumentParser(prog='test-evaluator', description=DESC)
    parser.add_argument('SUMMARIZED_FILE', type=str, help=SUMMARIZED_FILE_DESC)
    parser.add_argument('ORIGINAL_FILE', type=str, help=ORIGINAL_FILE_DESC)
    args = parser.parse_args()

    # obtain sentences and sentence labels
    sentences, sentences_rank = extract_text(args.ORIGINAL_FILE)

    # read summary
    summary_sentences = None
    with open(args.SUMMARIZED_FILE, 'r') as infile:
        summary_sentences = [sentence.rstrip() for sentence in infile]

    # obtain sentence labels of sentences in summary
    sentence_label_count = {}
    for sentence in summary_sentences:
        index = str(sentences_rank[sentence])
        sentence_label_count[index] = 1 if index not in sentence_label_count else sentence_label_count[index] + 1

    # print sentence label counts
    for sentence_label, count in sentence_label_count.items():
        print('Sentence Label: ' + sentence_label + ' / Count: ' + str(count))