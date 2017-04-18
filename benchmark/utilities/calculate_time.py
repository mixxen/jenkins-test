"""
calculate_time.py

Decorator to find out the time taken for a function to execute

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

from __future__ import division
import time
from guppy import hpy


def find_time(method):

    def timed(*args, **kwargs):
        total, memory = [], []
        loops = 5

        # to measure the memory or virtual memory used
        h = hpy()

        # to reduce the time involed in calculating memory
        diff = 0.0836183111810684159

        for i in range(loops):
            time_start = time.time()

            # executes the function
            result = method(*args, **kwargs)

            # calculater the memory used
            mem = h.heap().size
            time_taken = time.time() - time_start

            print 'Time taken - {a} of {l} loops: {t}'\
                '\tMemory used - {a} of {l} loops: {m}'.format(a=i + 1, l=loops, t=time_taken, m=mem)
            total.append(abs(time_taken - diff))
            memory.append(mem)

        return {
            'time':
                {
                    'best': min(total),
                    'worst': max(total),
                    'average': sum(total) / len(total)
                },
            'memory':
                {
                    'best': min(memory),
                    'worst': max(memory),
                    'average': sum(memory) / len(memory)
                }
        }

    return timed
