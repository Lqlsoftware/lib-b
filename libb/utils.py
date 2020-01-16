import sys

# load matrix from a file
def LoadMatrix(src=sys.stdin, dst=[], dtype=int):
    col_num, row_num = 0, 0
    for idx, line in enumerate(src):
        # readline from src and split by ' '
        line = line.rstrip('\n').split()
        # end of input
        if len(line) == 0:
            break
        # col's num is not unique
        elif idx != 0 and len(line) != col_num:
            exit('Expect a "matrix"!')
        col_num = len(line)
        # append to dst
        dst.append([dtype(e) for e in line])
        # count for row's num
        row_num += 1
    return dst, row_num, col_num

# print matrix M
def PrintMatrix(M, title=""):
    print(title)
    if type(M[0][0]) == float:
        for i in range(len(M)):
            print("|", end='')
            for j in range(len(M[i])):
                print("%10.6f" % M[i][j], end=', ')
            print("\b\b  |")
        print()
    else:
        for i in range(len(M)):
            print("|", end='')
            for j in range(len(M[i])):
                print("%7.6s" % M[i][j], end=', ')
            print("\b\b  |")
        print()

def RoundMatrix(M, digits=32):
    precision = 10 ** (-digits)
    for i in range(len(M)):
        for j in range(len(M[i])):
            e = round(M[i][j], digits)
            if abs(e) < precision:
                M[i][j] = 0.
            else:
                M[i][j] = e
    return M