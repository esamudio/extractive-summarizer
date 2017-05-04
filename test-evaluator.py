#!/usr/bin/env python3

import argparse
from os import walk
from utils import extract_text

# constants
DESC = '''This application evaluates our LexRank summarizer using the sentence labels provided in the dataset.'''
SUMMARIES_DIRECTORY_DESC = '''Directory containing original and summarized (.summary) files.'''

if __name__ == '__main__':
    # setup argument parser
    parser = argparse.ArgumentParser(prog='test-evaluator', description=DESC)
    parser.add_argument('SUMMARIES_DIRECTORY', type=str, help=SUMMARIES_DIRECTORY_DESC)
    args = parser.parse_args()
    overall_sentence_labels = {}
    sentence_label_count = {}

    path = args.SUMMARIES_DIRECTORY
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            if filename.endswith('.summary'):
                continue
            # obtain sentences and sentence labels
            # sentences, sentences_rank = extract_text(args.ORIGINAL_FILE)
            sentences, sentences_rank = extract_text(path + filename)
            # read summary
            summary_sentences = None
            with open(path + filename + '.summary', 'r') as infile:
                summary_sentences = [sentence.rstrip() for sentence in infile]

            # obtain sentence labels of sentences in summary
            for sentence in summary_sentences:
                index = str(sentences_rank[sentence])
                sentence_label_count[index] = 1 if index not in sentence_label_count else sentence_label_count[index] + 1

            # add them up for overall count
            for sentence, sentence_label in sentences_rank.items():
                index = str(sentence_label)
                overall_sentence_labels[index] = 1 if index not in overall_sentence_labels else overall_sentence_labels[
                                                                                              index] + 1

    print("Accuracy:")
    for sentence_label, count in sentence_label_count.items():
        print('Sentence Label: ' + sentence_label + ' / Count: ' + str(count/overall_sentence_labels[sentence_label]))
