# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Plotting code will be here once the migration from R is complete.

import matplotlib.pyplot as plt

def scatter_plot_2D(x, y, line, dot_color='black', line_color='blue'):
    plt.scatter(x, y, color='black')
    plt.plot(x, linear(x, y), color='blue', linewidth=3)
    plt.savefig(get_file_name("linear"))
    plt.clf()
