# LIB-B

A library contains implements of factorization supporting multiple methods and data types.

- LU Factorization
- Schmidt Decomposition (classical/modified)
- Householder Reduction
- Givens Reduction

## Environment

    Python 3.7.4 or higher

## Example

Clone this repo and open its dir, then run:

```sh
# python3 example.py lu|cs|ms|h|g
```

Or if you have some matrix file which is split by white space:

```sh
# python3 example.py -f matrix lu|cs|ms|h|g
```

## Usage

Import this package:

```python
import libb.factorization as lbb
```

Apply methods on matrix and fetch the result:

```python
P, L, U = lbb.LUFactorization(A=A_matrix)
Q, R = lbb.ClassicalSchmidtDecomposition(A=A_matrix)
Q, R = lbb.ModifiedSchmidtDecomposition(A=A_matrix)
Q, R = lbb.HouseholderReduction(A=A_matrix)
Q, R = lbb.GivensReduction(A=A_matrix)
```
