# -*- coding: utf-8 -*-
import numpy as np
from sympy import Matrix
from sympy.solvers.solvers import solve_linear_system_LU

# sequence = []
# for n in range(1, 10):
#     tot = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
#     sequence.append(tot)
#
# print sequence

sequence = [1, 683, 44287, 838861, 8138021, 51828151, 247165843, 954437177, 3138105961, 9090909091, 23775972551]
# sequence = [1, 8, 27, 64, 125, 216]

def termsInSequence(solution, terms):
    seq = []
    for n in range(1, terms):
        tot = 0
        for i in range(0, len(solution)):
            tot += solution[i] * (n ** i)
        seq.append(tot)
    return seq

def OP(k):
    matrix = []
    for n in range(1,k+1):
        row = []
        for i in range(0, k):
            row.append(n**i)
        matrix.append(row)
    return matrix

order = ['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
sumOfWrongs = 0
for j in range(1, 11):
    a = OP(j)
    b = sequence[0:j]
    # print a, b
    # x = np.linalg.solve(a, b)

    for i in range(0, len(b)):
        a[i].append(b[i])

    y = solve_linear_system_LU(Matrix(a), order)

    solution = []
    for value in order:
        if (value in y):
            solution.append(y[value])

    sumOfWrongs+= termsInSequence(solution, j+2)[-1]
    print termsInSequence(solution, j+2)
print sumOfWrongs


# OP(1, n) = x0*(n ** 0)
# [1] = 1

# OP(2, n) = x0*(n ** 0) + x1*(n ** 1)
# [1, 1] = 1
# [1, 2] = 8

# OP(3, n) = x0*(n ** 0) + x1*(n ** 1) + x2*(n ** 2)
# [1, 1, 1] = 1
# [1, 2, 4] = 8
# [1, 3, 9] = 27

# OP(4, n) = x0*(n ** 0) + x1*(n ** 1) + x2*(n ** 2) + x3*(n ** 3)
# [1, 1, 1, 1] = 1
# [1, 2, 4, 8] = 8
# [1, 3, 9, 27] = 27
# [1, 4, 16, 64] = 64
