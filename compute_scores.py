
def train_scores(list_of_sentences, cosine_threshold):
    """

    :param list_of_sentences: An array S of n sentences
    :param cosine_threshold: cosine threshold, t,
    :return An array of L of LexRank scores.

    """
    n = len(list_of_sentences)
    cosine_matrix = {}  # size n*n
    degree = {}  # size n
    L = {}  # size n

    for i in range(n):  # for i <- 1 to n do...
        for j in range(n):  # for j <- 1 to n do...
            cosine_tuple = (i, j)
            cosine_matrix[cosine_tuple] = idf-modified-cosine(list_of_sentences[i], list_of_sentences[j])
            # TODO: idf-modified-cosine(sentence[i], sentence[j])
            if cosine_matrix[cosine_tuple] > cosine_threshold:
                cosine_matrix[cosine_tuple] = 1
                if i not in degree:
                    degree[i] = 1
                else:
                    degree[i] += 1
            else:
                cosine_matrix[cosine_tuple] = 0
    # end
    for i in range(n):  # for i <- 1 to n do...
        for j in range(n):  # for j <- 1 to n do...
            cosine_tuple = (i, j)
            cosine_matrix[cosine_tuple] = cosine_matrix[cosine_tuple]/degree[i]     # might need to handle degree[i]
    # end
    # TODO: Error Tolerance
    L = PowerMethod(cosine_matrix, n, error_tolerance)    # TODO: PowerMethod(cosine_matrix, n, e)
    return L


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









if __name__ == '__main__':
    list_of_sentences = []
    cosine_threshold = 1
    train_scores(list_of_sentences, cosine_threshold)
