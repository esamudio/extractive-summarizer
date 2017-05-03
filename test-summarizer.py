import argparse
from utils import load_file

# constants
DESC = '''This application summarizes a given article using previously calculated inverse document frequencies (idf).'''

IDF_FILE_DESC = '''File containing idf values of words seen in training.'''

ORIGINAL_FILE_DESC = '''Name of file to summarize.'''

# setup argument parser
parser = argparse.ArgumentParser(prog='test-summarizer', description=DESC)
parser.add_argument('IDF_FILE', type=str, help=IDF_FILE_DESC)
parser.add_argument('ORIGINAL_FILE', type=str, help=ORIGINAL_FILE_DESC)
args = parser.parse_args()

words_idf = load_file(args.IDF_FILE)
