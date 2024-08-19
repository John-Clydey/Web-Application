import numpy as np

def inverse_matrices(matrix_A, matrix_B):
    if matrix_A.shape[0] != matrix_A.shape[1] or matrix_B.shape[0] != matrix_B.shape[1]:
        return "Matrices must be square."
    if np.linalg.det(matrix_A) == 0 or np.linalg.det(matrix_B) == 0:
        return "One or both matrices are singular and do not have inverses."

    inverse_matrix_A: np.linalg.inv(matrix_A)
    inverse_matrix_B: np.linalg.inv(matrix_B)

    combined_matrix = np.block([[matrix_A, inverse_matrix_A], [matrix_B, inverse_matrix_B]])
    return combined_matrix

