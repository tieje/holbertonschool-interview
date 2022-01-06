#!/usr/bin/python3
from math import log2
'''
Determine minimum number of operations to return n.
For n < 0 return 0
'''
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def PowerOf2Test(n):
    '''
    Tests if number is a power of 2.
    '''
    return(log2(n) % 1 == 0)


def minOpsHelper(n):
    '''
    Min ops helper
    '''
    if n in primes:
        return(n)
    decrement = n - 1
    ops = 0
    while decrement > 1:
        if n % decrement == 0:
            ops = n / decrement
            break
        decrement -= 1
    if decrement == 1:
        primes.append(n)
        return(n)
    return(ops + minOpsHelper(decrement))


def minOperations(n):
    '''
    Main func that runs some initial tests
    prior to the helper.
    '''
    if n <= 1 or type(n) != int:
        return(0)
    if PowerOf2Test(n):
        return(int(log2(n) * 2))
    return(int(minOpsHelper(n)))
