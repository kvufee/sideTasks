matrixA = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrixB = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

def matrixMultiplication(matrixA, matrixB):
    
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for m in range(len(matrixA)):
        for n in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                result[m][n] += matrixA[m][k] * matrixB[k][n]

    for i in result:
        print(i)