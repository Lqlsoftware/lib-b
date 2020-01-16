from libb.exception import SigularMatrixError, NotSquareMatrixError
from libb.utils import RoundMatrix


def LUFactorization(A, eType=float, digits=12):
    """LU Factorization

    Use Gaussian Elimination to apply LU Factorization on given square matrix A.

    Args:
        A:      A square matrix instance.
        eType:  Optional, the dtype of elements in matrix.
        digits: Optional, the digits of precision in float calculation.

    Returns:
        Three matrix: P, L, U which is the LU factorization of A.
    """

    # get size of A
    size = len(A)
    c_size = len(A[0])
    # check whether A is a square matrix or not
    if c_size != size:
        raise NotSquareMatrixError('Except a square matrix with shape (%d,%d) not (%d, %d)' % (size, size, size, c_size))

    # make a identity matrix as L
    L = [[eType(0) for j in range(size)] for i in range(size)]
    # deepcopy A as U with element type
    U = [[eType(A[i][j]) for j in range(size)] for i in range(size)]
    # make a size array as P which contains each row's number
    P = [i for i in range(size)]
    # do Gaussian elimination with Type III operations
    for i in range(size):
        # select max_abs element as pivot and interexchange its row with the i-th row
        max_idx = i
        for j in range(i + 1, size):
            if U[max_idx][i] == eType(0):
                max_idx = j
            elif abs(U[max_idx][i]) < abs(U[j][i]):
                max_idx = j
        if U[max_idx][i] == eType(0) or abs(U[max_idx][i]) < eType(1e-12):
            raise SigularMatrixError("LU Factorization cannot apply on a sigular matrix.")

        # exchange row i and row j
        U[i], U[max_idx] = U[max_idx], U[i]
        L[i], L[max_idx] = L[max_idx], L[i]
        P[i], P[max_idx] = P[max_idx], P[i]
        # do elimination to i + 1 ~ size row
        for j in range(i + 1, size):
            # calculate multiplier
            m = U[j][i] / U[i][i]
            # save multiplier in L
            L[j][i] = m
            # set directly to 0
            U[j][i] = eType(0)
            # update other row
            for k in  range(i + 1, size):
                U[j][k] = U[j][k] - m * U[i][k]
    # save 1 for diag in L
    for i in range(size):
        L[i][i] = eType(1)
    # construct P
    P = [[eType(1) if j == P[i] else eType(0) for j in range(size)] for i in range(size)]

    # Round matrix according to digits
    if eType == float:
        return RoundMatrix(P, digits), RoundMatrix(L, digits), RoundMatrix(U, digits)
    else:
        return P, L, U


def ClassicalSchmidtDecomposition(A, eType=float, digits=12):
    """Classical Schmidt Decomposition

    Use Gram-Schmidt orthogonal to generate the decomposition of given square matrix A.

    Args:
        A:      A square matrix instance.
        eType:  Optional, the dtype of elements in matrix.
        digits: Optional, the digits of precision in float calculation.

    Returns:
        Two matrix: Q, R which is the Classical Schmidt Decomposition of A.
    """

    # get size of A
    size = len(A)
    c_size = len(A[0])
    # check whether A is a square matrix or not
    if c_size != size:
        raise NotSquareMatrixError('Except a square matrix with shape (%d,%d) not (%d, %d)' % (size, size, size, c_size))

    # Define Q,R as zero matrix
    Q = [[eType(0) for j in range(size)] for i in range(size)]
    R = [[eType(0) for j in range(size)] for i in range(size)]
    for i in range(size):
        # copy x to u
        u = [eType(A[j][i]) for j in range(size)]

        # ui = ui - sum(qk * qk* * xi)    (0 <= k < i)
        for k in range(0, i):
            # rik = qk* * xi
            r_ik = eType(0)
            for j in range(size):
                r_ik += Q[j][k] * eType(A[j][i])
            R[k][i] = r_ik
            # ui = ui - rik * qk
            for j in range(size):
                u[j] -= r_ik * Q[j][k]

        # vii <- ||ui||
        u_norm_2 = eType(0)
        for j in range(size):
            u_norm_2 += u[j] * u[j]
        v_ii = u_norm_2 ** 0.5
        R[i][i] = v_ii

        # Have dependent columns
        if v_ii == eType(0) or abs(v_ii) < eType(1e-12):
            raise SigularMatrixError("Schmidt Decomposition cannot apply on a sigular matrix.")

        # qi <- ui / ||ui||
        for j in range(size):
            Q[j][i] = u[j] / v_ii

    # Round matrix according to digits
    if eType == float:
        return RoundMatrix(Q, digits), RoundMatrix(R, digits)
    else:
        return Q, R


def ModifiedSchmidtDecomposition(A, eType=float, digits=12):
    """Modified Schmidt Decomposition

    Use Gram-Schmidt orthogonal to generate the decomposition of given square matrix A.

    Args:
        A:      A square matrix instance.
        eType:  Optional, the dtype of elements in matrix.
        digits: Optional, the digits of precision in float calculation.

    Returns:
        Two matrix: Q, R which is the Modified Schmidt Decomposition of A.
    """

    # get size of A
    size = len(A)
    c_size = len(A[0])
    # check whether A is a square matrix or not
    if c_size != size:
        raise NotSquareMatrixError('Except a square matrix with shape (%d,%d) not (%d, %d)' % (size, size, size, c_size))

    # Deep copy an eType transpose A instance
    U = [[eType(A[j][i]) for j in range(size)] for i in range(size)]
    # Define Q,R as zero matrix
    Q = [[eType(0) for j in range(size)] for i in range(size)]
    R = [[eType(0) for j in range(size)] for i in range(size)]
    for i in range(size):
        # vii <- ||ui||
        u_norm_2 = eType(0)
        for j in range(size):
            u_norm_2 += U[i][j] * U[i][j]
        v_ii = u_norm_2 ** 0.5
        R[i][i] = v_ii

        # qi <- ui / ||ui||
        for j in range(size):
            Q[j][i] = U[i][j] / v_ii

        # uk = uk - qi * qi* * xk)    (0 <= i < k < size)
        for k in range(i + 1, size):
            # rki = qi* * xk
            r_ki = eType(0)
            for j in range(size):
                r_ki += Q[j][i] * eType(A[j][k])
            R[i][k] = r_ki
            # uk = uk - rik * qi
            for j in range(size):
                U[k][j] -= r_ki * Q[j][i]

    # Round matrix according to digits
    if eType == float:
        return RoundMatrix(Q, digits), RoundMatrix(R, digits)
    else:
        return Q, R


def HouseholderReduction(A, eType=float, digits=12):
    """Householder Reduction

    Use reflex matrix to reduct given square matrix A to QR.

    Args:
        A:      A square matrix instance.
        eType:  Optional, the dtype of elements in matrix.
        digits: Optional, the digits of precision in float calculation.

    Returns:
        Two matrix: Q, R which is the decomposition of A.
    """

    # get size of A
    size = len(A)
    c_size = len(A[0])
    # check whether A is a square matrix or not
    if c_size != size:
        raise NotSquareMatrixError('Except a square matrix with shape (%d,%d) not (%d, %d)' % (size, size, size, c_size))

    # Define Q as identity matrix
    Q = [[eType(1) if i == j else eType(0) for j in range(size)] for i in range(size)]
    # Define R as a deep copy of A
    R = [[eType(A[i][j]) for j in range(size)] for i in range(size)]
    for i in range(size - 1):
        # length of u1
        length = size - i
        # define u1
        u = [R[j][i] for j in range(i, size)]
        # u1 <- x1 - ||ui||e1
        x_norm_2 = eType(0)
        for j in range(length):
            x_norm_2 += u[j] * u[j]
        x_norm = x_norm_2 ** 0.5
        u[0] -= x_norm

        # Pi = I - 2/ui(ui*) * (ui*)ui
        # define P as identity matrix, P = I.
        P = [[eType(0) if k != j else eType(1) for j in range(length)] for k in range(length)]
        # c = 2/ui(ui*)
        u_norm_2 = eType(0)
        for j in range(length):
            u_norm_2 += u[j] * u[j]
        c = eType(2) / u_norm_2
        # Pi = Pi - c * (ui*)ui
        for j in range(length):
            for k in range(length):
                P[j][k] -= c * u[j] * u[k]
        # TODO Parallel {R = Ri' * Ai} & {Q = Ri' * Q_i}
        # R = Ri' * R
        #  Update the right bottom of R
        #  R = | R1  R2 |   Ri' = | 1  0  |  Ai = | R4 |
        #      | 0   R4 |         | 0  Ri |
        #
        #  Ri' * R = | R1  R2   |
        #            | 0   RiR4 |
        #
        A_i = [[R[k][j] for j in range(i, size)] for k in range(i, size)]
        # Ri * R_i
        for j in range(length):
            for k in range(length):
                r, c = j + i, k + i
                R[r][c] = eType(0)
                for l in range(length):
                    R[r][c] += P[j][l] * A_i[l][k]

        # Q = Ri' * Q_i
        #  Update the left bottom & the right bottom of Q
        #  Q = | Q1  Q2 |   Ri' = | 1  0  |  Qi = | Q3  Q4 |
        #      | Q3  Q4 |         | 0  Ri |
        #
        #  Ri' * Q = | Q1   Q2   |
        #            | RiQ3 RiQ4 |
        #
        Q_i = [[Q[k][j] for j in range(size)] for k in range(i, size)]
        for j in range(length):
            for k in range(size):
                Q[j + i][k] = eType(0)
                for l in range(length):
                    Q[j + i][k] += P[j][l] * Q_i[l][k]

    # Q = Q.transpose (Q is PnPn-1...P2P1)
    for j in range(size):
        for k in range(j + 1, size):
            Q[k][j], Q[j][k] = Q[j][k], Q[k][j]

    # Round matrix according to digits
    if eType == float:
        return RoundMatrix(Q, digits), RoundMatrix(R, digits)
    else:
        return Q, R


def GivensReduction(A, eType=float, digits=12):
    """Givens Reduction

    Use rotation matrix to reduct given square matrix A to QR.

    Args:
        A:      A square matrix instance.
        eType:  Optional, the dtype of elements in matrix.
        digits: Optional, the digits of precision in float calculation.

    Returns:
        Two matrix: Q, R which is the decomposition of A.
    """

    # get size of A
    size = len(A)
    c_size = len(A[0])
    # check whether A is a square matrix or not
    if c_size != size:
        raise NotSquareMatrixError('Except a square matrix with shape (%d,%d) not (%d, %d)' % (size, size, size, c_size))

    # Define Q as identity matrix
    Q = [[eType(1) if i == j else eType(0) for j in range(size)] for i in range(size)]
    # Define R as a deep copy of A
    R = [[eType(A[i][j]) for j in range(size)] for i in range(size)]
    for i in range(size - 1):
        for j in range(i + 1, size):
            # annihilate A_ji (i < j)
            # define P_ij as identity matrix
            P_ij = [[eType(1) if i == j else eType(0) for j in range(size)] for i in range(size)]
            cs_root_square = (R[i][i] * R[i][i] + R[j][i] * R[j][i]) ** 0.5
            c = R[i][i] / cs_root_square
            s = R[j][i] / cs_root_square
            # update P (i,i) = c (i,j) = s (j,i) = -s (j,j) = c
            P_ij[i][i] = c
            P_ij[i][j] = s
            P_ij[j][i] = -s
            P_ij[j][j] = c

            # apply P_ij on A(R) to annihilate A_ji
            # R_temp = P_ij * R
            R_temp = [[eType(0) for j in range(size)] for i in range(size)]
            for k in range(size):
                for l in range(size):
                    for m in range(size):
                        R_temp[k][l] += P_ij[k][m] * R[m][l]
            R = R_temp
            # apply P_ij on Q to generate next Q
            # Q_temp = P_ij * Q
            Q_temp = [[eType(0) for j in range(size)] for i in range(size)]
            for k in range(size):
                for l in range(size):
                    for m in range(size):
                        Q_temp[k][l] += P_ij[k][m] * Q[m][l]
            Q = Q_temp

    # Q = Q.transpose (Q is PnPn-1...P2P1)
    for j in range(size):
        for k in range(j + 1, size):
            Q[k][j], Q[j][k] = Q[j][k], Q[k][j]

    # Round matrix according to digits
    if eType == float:
        return RoundMatrix(Q, digits), RoundMatrix(R, digits)
    else:
        return Q, R

