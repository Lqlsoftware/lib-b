import sys
import factorization as fc
from dtype import Fraction
from utils import LoadMatrix
from utils import PrintMatrix

if __name__ == "__main__":
    if len(sys.argv) != 1:
        f = open(sys.argv[1], 'r+')
    else:
        f = sys.stdin
    # load matrix from sys.stdin or some opened file
    A_matrix, row_num, col_num = LoadMatrix(src=f, dst=[], dtype=int)
    # make sure A is a square matrix
    if row_num != col_num:
        exit('Expect a "square" matrix')
    PrintMatrix(M=A_matrix, title="A:")

    # LU Factorization
    print("LU Factorization")
    P, L, U = fc.LUFactorization(A=A_matrix, eType=float)
    PrintMatrix(M=P, title="P:")
    PrintMatrix(M=L, title="L:")
    PrintMatrix(M=U, title="U:")

    # Classical Schmidt Decomposition
    print("Classical Schmidt Decomposition")
    Q, R = fc.ClassicalSchmidtDecomposition(A=A_matrix)
    PrintMatrix(M=Q, title="Q:")
    PrintMatrix(M=R, title="R:")

    # Modified Schmidt Decomposition
    print("Modified Schmidt Decomposition")
    Q, R = fc.ModifiedSchmidtDecomposition(A=A_matrix)
    PrintMatrix(M=Q, title="Q:")
    PrintMatrix(M=R, title="R:")

    # Householder Reduction
    print("Householder Reduction")
    Q, R = fc.HouseholderReduction(A=A_matrix)
    PrintMatrix(M=Q, title="Q:")
    PrintMatrix(M=R, title="R:")

    # Givens Reduction
    print("Givens Reduction")
    Q, R = fc.GivensReduction(A=A_matrix)
    PrintMatrix(M=Q, title="Q:")
    PrintMatrix(M=R, title="R:")