# LIB-B

A library contains implements of factorization supporting multiple methods and data types.

- LU Factorization
- Schmidt Decomposition (classical/modified)
- Householder Reduction
- Givens Reduction

## Environment

    Python 3.4 or higher

## Install

```sh
pip install lib-b
```

## Usage

```sh
# libb -h
```

Apply all decomposition on the matrix you input:

```sh
# libb lucsmshg
```

## Usage in script

Import it:

```python
import libb
```

Load matrix(from stdin or opened file):
```python
A_matrix, row_num, col_num = libb.LoadMatrix(src=stdin)
```

Apply methods on matrix (any struct that supports index operator `[]`) and fetch the result:

```python
P, L, U = libb.LUFactorization(A=A_matrix)
Q, R = libb.ClassicalSchmidtDecomposition(A=A_matrix)
Q, R = libb.ModifiedSchmidtDecomposition(A=A_matrix)
Q, R = libb.HouseholderReduction(A=A_matrix)
Q, R = libb.GivensReduction(A=A_matrix)
```
