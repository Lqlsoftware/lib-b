# Factorizations Utils

A implement of factorization support by multiple methods and data types.

- LU Factorization
- Schmidt Decomposition (classical/modified)
- Householder Reduction
- Givens Reduction

## Environment

    Python 3.7.4 or higher

## Example

Clone this repo and open its dir, then run:

```sh
# python3 example.py
```

Or if you have some matrix file which is split by white space:

```sh
# python3 example.py matrix
```

## Usage

Import this package:

```python
    import Factorization.factorization as fc
```

Apply methods on matrix and fetch the result:

```python
P, L, U = fc.LUFactorization(A=A_matrix)
Q, R = fc.ClassicalSchmidtDecomposition(A=A_matrix)
Q, R = fc.ModifiedSchmidtDecomposition(A=A_matrix)
Q, R = fc.HouseholderReduction(A=A_matrix)
Q, R = fc.GivensReduction(A=A_matrix)
```