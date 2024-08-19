import numpy as np
def transpose(mat_A):
    j = mat_A.shape[0]
    p = mat_A.shape[1]
    mat_Id = np.zeros((p, j))

    for i in range(j):
        for j in range(p):
            mat_Id[j][i] = mat_A[i][j]
    return mat_Id

