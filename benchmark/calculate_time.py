"""
calculate_time.py

Decorator to find out the time taken for a function to execute

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

from __future__ import division
import time


def find_time(method):

    def timed(*args, **kwargs):
        total = []
        loops = 5
        for i in range(loops):
            time_start = time.time()
            result = method(*args, **kwargs)
            time_taken = time.time() - time_start

            print 'Time taken - {a} of {l} loops: {t}'.format(a=i + 1, l=loops, t=time_taken)
            total.append(time_taken)

        return {
            'best': min(total),
            'worst': max(total),
            'average': sum(total) / len(total)
        }

    return timed
