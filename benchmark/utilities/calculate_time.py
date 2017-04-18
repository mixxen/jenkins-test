"""
calculate_time.py

Decorator to find out the time taken for a function to execute

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

from __future__ import division
import time
import resource

from guppy import hpy


def find_time(method):

    def timed(*args, **kwargs):
        total, memory, sys_time, user_time = [], [], [], []
        loops = 5

        # to measure the memory or virtual memory used
        h = hpy()

        # to reduce the time involed in calculating memory
        diff = 0.00836183111810684159

        for i in range(loops):

            # calculate the start time and the resource usage
            start_time, start_resources = time.time(), resource.getrusage(resource.RUSAGE_SELF)

            # executes the function
            result = method(*args, **kwargs)

            # calculate the end time and the resource usage
            end_resources, end_time = resource.getrusage(resource.RUSAGE_SELF), time.time()

            # calculater the memory used
            mem = h.heap().size
            time_taken = end_time - start_time
            sys_t = end_resources.ru_stime - start_resources.ru_stime
            user_t = end_resources.ru_utime - start_resources.ru_utime

            print 'For {a} of {l} loops' \
                '\tTime taken: {t}' \
                '\tSystem time: {s}' \
                '\tUser time: {u}' \
                '\tMemory used: {m}'.format(a=i + 1, l=loops, t=time_taken,
                                            m=mem, s=sys_t, u=user_t)

            total.append(abs(time_taken - diff))
            sys_time.append(sys_t)
            user_time.append(user_t)
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
                },
            'sys_time':
                {
                    'best': min(sys_time),
                    'worst': max(sys_time),
                    'average': sum(sys_time) / len(sys_time)
                },
            'user_time':
                {
                    'best': min(user_time),
                    'worst': max(user_time),
                    'average': sum(user_time) / len(user_time)
                },
        }

    return timed
