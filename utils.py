

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

    url, sentences, highlights, maps = text.split('\n\n')

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
