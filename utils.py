from collections import defaultdict
from os import walk

def idf_modified_cosine():



def PowerMethod(cosine_matrix, matrix_size, error_tolerance):
    """

    :param cosine_matrix: Cosine Matrix from train_scores
    :param matrix_size: Size of the matrix(sentence)
    :param error_tolerance: Error tolerance
    :return eigenvector p
    """

    t = 0
    while (result < error_tolerance):
        t += 1
        # TODO: Finish Algorithm 2


def train_scores(sentences, cosine_threshold):
    """

    :param sentences: An array S of n sentences
    :param cosine_threshold: cosine threshold, t,
    :return An array of L of LexRank scores.

    """
    n = len(sentences)
    cosine_matrix = {}  # size n*n
    degree = {}  # size n
    L = {}  # size n

    for i in range(n):  # for i <- 1 to n do...
        for j in range(n):  # for j <- 1 to n do...
            cosine_tuple = (i, j)
            # TODO: idf_modified_cosine(sentence[i], sentence[j])
            cosine_matrix[cosine_tuple] = idf_modified_cosine(sentences[i], sentences[j])
            if cosine_matrix[cosine_tuple] > cosine_threshold:
                cosine_matrix[cosine_tuple] = 1
                degree[i] = 1 if i not in degree else degree[i]+1
            else:
                cosine_matrix[cosine_tuple] = 0
    # end
    for i in range(n):  # for i <- 1 to n do...
        for j in range(n):  # for j <- 1 to n do...
            cosine_tuple = (i, j)
            cosine_matrix[cosine_tuple] = cosine_matrix[cosine_tuple]/degree[i]     # might need to handle degree[i]
    # end
    # TODO: Error Tolerance
    # TODO: PowerMethod(cosine_matrix, n, e)
    L = PowerMethod(cosine_matrix, n, error_tolerance)
    return L


def extract_text(filename):
    """
    This function processes articles from the CNN dataset, extracts all the sentences in a list
    along with a dictionary that maps the sentences with their respective sentence labels.
    :param filename: name of file with text to summarize
    :type filename: str
    :return: list of sentences and a dictionary that maps each sentence with their respective sentence label
    :rtype: list, list of tup
    """
    text = ''
    with open('../neuralsum/cnn/training/' + filename, 'r') as infile:
        text = ''.join(infile.readlines())
    text_tokens = text.split('\n\n')
    url=sentences=highlights=maps=''
    if len(text_tokens) == 4:
        url, sentences, highlights, maps = text_tokens
    else:
        url = text_tokens[0]
        sentences = text_tokens[1]
        highlights = text_tokens[2]
        for i in range(3, len(text_tokens)):
            maps += text_tokens[i] + '\n'
        else:
            maps = maps[:-1]

    # entities
    entities = {mapping.split(':')[0]:mapping.split(':')[1] for mapping in maps.split('\n')}

    # sentences
    processed_sentences = []
    entity_tag = '@entity'
    while entity_tag in sentences:
        start_index = sentences.find(entity_tag)
        end_index = start_index + len(entity_tag)
        while sentences[end_index+1].isdigit():
            end_index += 1
        entity = sentences[start_index:end_index+1]
        sentences = sentences.replace(entity, entities[entity])
    sentences_rank = {token.split('\t\t\t')[0]: token.split('\t\t\t')[1] for token in (sentence for sentence in sentences.split('\n'))}
    sentences = [sentence for (sentence, rank) in sentences_rank.items()]
    return sentences, sentences_rank

def word_counter(path):
    single_document_word_counts = {}
    multiple_document_word_count = defaultdict(float)
    number_of_documents = 0
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            sentences, sentences_rank = extract_text(filename)
            sentences = ' '.join(sentences)
            for word in sentences.split():
                if word not in single_document_word_counts:
                    single_document_word_counts[word] = 1
            for key in single_document_word_counts.keys():
                multiple_document_word_count[key] += 1
            single_document_word_counts = {}
            number_of_documents += 1
    return dict(multiple_document_word_count), number_of_documents