"""
algo_list.py

Has the list of algorithms of a single user
This is for testing purpose only.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""


def algo1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/2073279#2073279
    """ Returns  a list of primes < n """
    numbers = range(3, n + 1, 2)
    half = (n) // 2
    initial = 4

    for step in xrange(3, n + 1, 2):
        for i in xrange(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)

        if initial > half:
            return [2] + filter(None, numbers)


def algo2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n / 2)
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i / 2]:
            sieve[i * i / 2::i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [2 * i + 1 for i in xrange(1, n / 2) if sieve[i]]


def algo3(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


def algo4(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """

    correction = (n % 6 > 1)
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n / 3)
    sieve[0] = False
    for i in xrange(int(n**0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) / 3)::2 * k] = [False] * ((n / 6 - (k * k) / 6 - 1) / k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) / 3::2 * k] = [False] * \
                ((n / 6 - (k * k + 4 * k - 2 * k * (i & 1)) / 6 - 1) / k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n / 3 - correction) if sieve[i]]
