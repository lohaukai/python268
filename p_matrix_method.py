def add_matrix(matrix1, matrix2):
    return_matrix = []
    for row in range(len(matrix1)):
        return_matrix.append([])
        for col in range(len(matrix2[row])):
            element = 0
            for cross in range(len(matrix2)):
                element += matrix1[row][cross] * matrix2[cross][col]
            return_matrix[row].append(element)
    return return_matrix


def input_matrix():
    create_matrix = []
    for row in range(3):  # set col size to 3
        create_matrix.append([])
        buf = str(input()).strip().split(' ')
        for col in range(len(buf)):
            create_matrix[row].append(eval(buf[col]))
    return create_matrix


A = input_matrix()
B = input_matrix()
C = add_matrix(A, B)
print('%-5d%-5d%-5d' % (C[0][0], C[0][1], C[0][2]))
print('%-5d%-5d%-5d' % (C[1][0], C[1][1], C[1][2]))
print('%-5d%-5d%-5d' % (C[2][0], C[2][1], C[2][2]))
