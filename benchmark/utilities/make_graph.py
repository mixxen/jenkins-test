"""
make_graph.py

Generates the graph of the results.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""
import matplotlib.pyplot as plt
import numpy as np


def generate_graph(results, algo_names):
    """Function to generate graph of the results"""
    fig = plt.figure(figsize=(18, 4), dpi=1600)

    alpha = 0.7
    colors = ['g', 'r', 'b']
    X = np.arange(len(algo_names))
    dists = [0, -0.25, 0.25]
    labels = ['Best', 'Worst', 'Average']
    x_vals = algo_names
    memory_list, time_list = [], []

    for __, values in results.iteritems():
        memory_list.append(values['memory'].values())
        time_list.append(values['time'].values())

    memory_transpose = zip(*memory_list)
    time_transpose = zip(*time_list)

    # algs_transpose = zip(
    #     *[[value for __, value in values.iteritems()]
    #       for __, values in results.iteritems()]
    # )

    ax1 = fig.add_subplot(121)
    for alg_t, color, dist, label in zip(time_transpose, colors, dists, labels):
        ax1.bar(X + dist, alg_t, width=0.2, color=color,
                align='center', label=label, alpha=alpha)

    plt.title('Algorithm\'s Benchmark - Time')
    plt.xticks(X, x_vals, rotation=45)
    plt.legend(loc='best')
    plt.ylabel('Time in milliseconds')
    plt.grid(True)
    ax1.margins(0.05)
    ax2 = fig.add_subplot(122)

    for alg_t, color, dist, label in zip(memory_transpose, colors, dists, labels):
        ax2.bar(X + dist, alg_t, width=0.2, color=color,
                align='center', label=label, alpha=alpha)

    plt.title('Algorithm\'s Benchmark - Memory')
    plt.xticks(X, x_vals, rotation=45)
    plt.legend(loc='best', bbox_to_anchor=(1, 1))
    plt.ylabel('Time in Bytes')
    plt.grid(True)
    ax2.margins(0.05)

    plt.savefig('results.png', bbox_inches='tight')
