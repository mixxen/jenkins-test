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
    fig.suptitle('Algorithm\'s Benchmark', fontsize=12)
    alpha = 0.7
    colors = ['g', 'r', 'b']
    X = np.arange(len(algo_names))
    dists = [0, -0.25, 0.25]
    labels = ['Best', 'Worst', 'Average']
    x_vals = algo_names
    memory_list, time_list, sys_time_list, user_time_list = [], [], [], []

    for __, values in results.iteritems():
        memory_list.append(values['memory'].values())
        time_list.append(values['time'].values())
        sys_time_list.append(values['sys_time'].values())
        user_time_list.append(values['user_time'].values())

    memory_transpose = zip(*memory_list)
    time_transpose = zip(*time_list)
    sys_time_transpose = zip(*sys_time_list)
    user_time_transpose = zip(*user_time_list)

    # algs_transpose = zip(
    #     *[[value for __, value in values.iteritems()]
    #       for __, values in results.iteritems()]
    # )

    ax1 = fig.add_subplot(141)

    for alg_t, color, dist, label in zip(time_transpose, colors, dists, labels):
        ax1.bar(X + dist, alg_t, width=0.2, color=color,
                align='center', label=label, alpha=alpha)

    plt.title('Time')
    plt.xticks(X, x_vals, rotation=45)
    plt.legend(loc='best')
    plt.ylabel('Time in milliseconds')
    plt.grid(True)
    ax1.margins(0.05)

    ax2 = fig.add_subplot(142)

    for alg_t, color, dist, label in zip(memory_transpose, colors, dists, labels):
        ax2.bar(X + dist, alg_t, width=0.2, color=color,
                align='center', label=label, alpha=alpha)

    plt.title('Memory')
    plt.xticks(X, x_vals, rotation=45)
    plt.legend(loc='best')
    plt.ylabel('Memory utilized in Bytes')
    plt.grid(True)
    ax2.margins(0.05)

    ax3 = fig.add_subplot(143)

    for alg_t, color, dist, label in zip(sys_time_transpose, colors, dists, labels):
        ax3.bar(X + dist, alg_t, width=0.2, color=color,
                align='center', label=label, alpha=alpha)

    plt.title('System Time')
    plt.xticks(X, x_vals, rotation=45)
    plt.legend(loc='best')
    plt.ylabel('Time in Seconds')
    plt.grid(True)
    ax3.margins(0.05)

    ax4 = fig.add_subplot(144)

    for alg_t, color, dist, label in zip(user_time_transpose, colors, dists, labels):
        ax4.bar(X + dist, alg_t, width=0.2, color=color,
                align='center', label=label, alpha=alpha)

    plt.title('User Time')
    plt.xticks(X, x_vals, rotation=45)
    plt.legend(loc='best')
    plt.ylabel('Time in Seconds')
    plt.grid(True)
    ax4.margins(0.05)

    plt.savefig('results.png', bbox_inches='tight')
