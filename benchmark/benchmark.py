"""
benchmark.py

Calculates the time taken by each algorithm

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import re
import importlib

from utilities.calculate_time import find_time


def generate_graph(results, algo_names):
    import matplotlib.pyplot as plt
    import numpy as np

    ax = plt.subplot(111)

    alpha = 0.7
    colors = ['g', 'r', 'b']
    X = np.arange(len(algo_names))
    dists = [0, -0.25, 0.25]
    labels = ['Best', 'Worst', 'Average']
    x_vals = algo_names
    algs_transpose = zip(
        *[[value for key, value in values.iteritems()]
          for alg_name, values in results.iteritems()]
    )

    for alg_t, color, dist, label in zip(algs_transpose, colors, dists, labels):
        ax.bar(X + dist, alg_t, width=0.2, color=color,
               align='center', label=label, alpha=alpha)

    plt.title('Algorithm\'s Benchmark')
    plt.xticks(X, x_vals, rotation=45)
    plt.legend(loc='best', bbox_to_anchor=(1, 1))
    plt.ylabel('Time in milliseconds')
    plt.grid(True)
    ax.margins(0.05)
    plt.savefig('results.png', bbox_inches='tight')


# from algo_list import *
# import algo_list
# Line 9 to 17 is the equivalent of above two lines,
# its helps us in adding files dynamically
algo_list = importlib.import_module('.' + 'algo_list', 'algorithms')
alg_dict = algo_list.__dict__

regex_pattern = re.compile(r'algo\d+')

# get the function names from the module
algo_names = [name for name in dir(algo_list)
              if regex_pattern.match(name)]

# updates the global method, with the function
# from imported module.
globals().update({name: alg_dict[name] for name in algo_names})

# adds decorator to all the functions
# no need to write the following:
# @find_time
# def algo1(n):
#     do something
# @find_time
# def algo2(n):
#     do something
for name in algo_names:
    globals()[name] = find_time(globals()[name])

results = {}

for alg in algo_names:
    print 'Time taken for {a}'.format(a=alg)
    results[alg] = globals()[alg](1000000)

print
print 'Overall Results'
print results

generate_graph(results, algo_names)
