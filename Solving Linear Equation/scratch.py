import numpy as np


# This function will compute the solution of a SLE
def get_solution(A, B):  # A and B are lists
    MatA = np.array(A)
    MatConst = np.array(B)
    solution = np.linalg.solve(MatA, MatConst)
    return solution


NumOfEquations = int(input("Enter number of Equations: "))

CoeffMatrix = []
Const = []
# Loop for inputting the coefficients and constant
for i in range(NumOfEquations):
    coeff = []
    for j in range(NumOfEquations):
        coeff.append(float(input(f'Enter the coefficient {j+1} of Equation-{i+1}: ')))
    CoeffMatrix.append(coeff)
    Const.append(float(input(f'Enter the constant of equation-{i+1}: ')))

Result = get_solution(CoeffMatrix, Const)
print(f"The solution of the SLE is {Result}!")