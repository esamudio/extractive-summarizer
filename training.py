# this file trains our model by counting the amount of times a given word was seen across all documents
from utils import word_counter
from math import log

word_counts, number_of_documents = word_counter('../neuralsum/cnn/training/')
with open('training-test.txt', 'w') as outfile:
    for key in word_counts.keys():
        outfile.write(
            key + '\t' + str(word_counts[key]) + '\t' + str(log(number_of_documents/word_counts[key])) + '\n'
        )
