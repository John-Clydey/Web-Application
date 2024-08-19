def sum_matrices(matrix_A, matrix_B):
    result = []
    for i in range(len(matrix_A)):
        row = []
        for j in range(len(matrix_A[0])):
            row.append(matrix_A[i][j] + matrix_B[i][j])
        result.append(row)
    return result
