#!/bin/python3

import math
import os
import random
import re
import sys




def prime_factors(n):
    factors = set() #Return the set of prime factors of n
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2
    if n > 1:
        factors.add(n)
    return factors
def euler_totient(n):
    result = n #Compute phi(n)
    for p in prime_factors(n):
        result -= result // p
    return result
def smallest_primitive_root(p):
    phi = p - 1
    factors = prime_factors(phi)
    for g in range(2, p):
        ok = True
        for q in factors:
            if pow(g, phi // q, p) == 1:
                ok = False
                break
        if ok:
            return g
if __name__ == '__main__':
    p = int(input().strip())

    g = smallest_primitive_root(p)
    count = euler_totient(p - 1)

    print(g, count)
