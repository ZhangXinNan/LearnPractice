
import random
random.seed(0)


def sigGen(matrix):
    """
    * generate the signature vector
    :param matrix: a ndarray var
    :return a signature vector: a list var
    """

    # the row sequence set
    seqSet = [i for i in range(matrix.shape[0])]
    print(seqSet)

    # initialize the sig vector as [-1, -1, ..., -1]
    result = [-1 for i in range(matrix.shape[1])]

    count = 0

    while len(seqSet) > 0:

        # choose a row of matrix randomly
        randomSeq = random.choice(seqSet)

        for i in range(matrix.shape[1]):

            if matrix[randomSeq][i] != 0 and result[i] == -1:
                result[i] = randomSeq
                count += 1
        print(randomSeq, result)
        if count == matrix.shape[1]:
            break

        seqSet.remove(randomSeq)

    # return a list
    return result

def sigMatrixGen(input_matrix, n):
    """
    generate the sig matrix
    :param input_matrix: naarray var
    :param n: the row number of sig matrix which we set
    :return sig matrix: ndarray var
    """

    result = []

    for i in range(n):
        sig = sigGen(input_matrix)
        result.append(sig)

    # return a ndarray
    print("\nsig matrix:")
    print(np.array(result))
    print()
    return np.array(result)

import numpy as np
mat = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0]])

print("input:")
print(mat)
print(mat.shape)

sigMatrixGen(mat, 4)