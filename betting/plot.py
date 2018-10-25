import matplotlib.pyplot as plt

def plot_graph(yLabel, xLabel, initial_funds):
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.axhline(0, color='r')
    plt.axhline(initial_funds, color='r')
    plt.show()
