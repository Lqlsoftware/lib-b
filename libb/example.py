import sys
import argparse

import libb.factorization as fc

from libb.dtype import Fraction
from libb.utils import LoadMatrix, PrintMatrix

def getArguments(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Matrix Decomposition Utils.")
    parser.add_argument(dest='method', help="decomposition method.", metavar= "lu|cs|ms|h|g")
    parser.add_argument("-f", "--file", dest='file', help="open a matrix file")
    parser.add_argument("-t", "--type", dest='etype', default='float', help="entries output type (default float)", metavar= "[float|frac]")
    return parser.parse_args(args)

if __name__ == "__main__":
    args = getArguments()
    # args.file
    if args.file == None:
        print("[INFO] Input matrix (split by white space):")
        f = sys.stdin
    else:
        f = open(args.file, 'r+')

    # args.etype
    if args.etype == 'frac':
        etype = Fraction
    else:
        etype = float

    # load matrix from sys.stdin or some opened file
    A_matrix, row_num, col_num = LoadMatrix(src=f, dst=[], dtype=int)

    # make sure A is a square matrix
    if row_num != col_num:
        exit('Expect a "square" matrix!')
    PrintMatrix(M=A_matrix, title="Matrix A:")

    # LU Factorization
    if args.method.find("lu") != -1:
        print("LU Factorization")
        P, L, U = fc.LUFactorization(A=A_matrix, eType=etype)
        PrintMatrix(M=P, title="P:")
        PrintMatrix(M=L, title="L:")
        PrintMatrix(M=U, title="U:")

    # Classical Schmidt Decomposition
    if args.method.find("cs") != -1:
        print("Classical Schmidt Decomposition")
        Q, R = fc.ClassicalSchmidtDecomposition(A=A_matrix, eType=etype)
        PrintMatrix(M=Q, title="Q:")
        PrintMatrix(M=R, title="R:")

    # Modified Schmidt Decomposition
    if args.method.find("ms") != -1:
        print("Modified Schmidt Decomposition")
        Q, R = fc.ModifiedSchmidtDecomposition(A=A_matrix, eType=etype)
        PrintMatrix(M=Q, title="Q:")
        PrintMatrix(M=R, title="R:")

    # Householder Reduction
    if args.method.find("h") != -1:
        print("Householder Reduction")
        Q, R = fc.HouseholderReduction(A=A_matrix, eType=etype)
        PrintMatrix(M=Q, title="Q:")
        PrintMatrix(M=R, title="R:")

    # Givens Reduction
    if args.method.find("g") != -1:
        print("Givens Reduction")
        Q, R = fc.GivensReduction(A=A_matrix, eType=etype)
        PrintMatrix(M=Q, title="Q:")
        PrintMatrix(M=R, title="R:")
