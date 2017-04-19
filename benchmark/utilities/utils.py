from __future__ import division
import time
import resource

import matplotlib.pyplot as plt
import numpy as np
from guppy import hpy


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


def find_time(method):
    """Decorator to find out the time taken for a function to execute"""
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


def split_train_test(X, y, limit, *args, **kwargs):
    """
    Splits the vector and target to training and testing

    Splitting the datasets into training and testing, does a cross validation

    Returns X_train, y_train, X_test, y_test
    """

    if len(X) == len(y):
        n_samples = len(X)
    else:
        raise Exception('The lengths of X and y does not match')

    precent_of_sample = int(limit * n_samples)
    X_train = X[:precent_of_sample]
    y_train = y[:precent_of_sample]
    X_test = X[precent_of_sample:]
    y_test = y[precent_of_sample:]

    return X_train, y_train, X_test, y_test
