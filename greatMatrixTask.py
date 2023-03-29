mx1 = list(map(int, input().split()))
mx2 = list(map(int, input().split()))

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
        

ans = matrixMultiplication(mx1, mx2)