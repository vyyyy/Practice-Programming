#Srinivasa Ramanujan's infinite series calculates an estimation of pi.

import math


def estimate_pi():

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    
    total = 0
    k = 0
    while True:
        factor = 2 * math.sqrt(2) / 9801
        numerator = factorial(4**k) * (1103 + 26390*k)
        denominator = factorial(k)**4 * 396**(4*k)
        x = factor * round(numerator / denominator)
        total += x

        if abs(x) < 1e-15:
            break
        k += 1

    return 1 / total

#let's test
print('estimate_pi:', estimate_pi())

#compare with math.pi built-in module
print('math.pi:', math.pi)
