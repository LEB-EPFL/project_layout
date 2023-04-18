from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fname = Path("experiments/analysis/2023-04-17-hela-trf2-clustering/results.csv")
    data = np.genfromtxt(fname, delimiter=",")

    _, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(data, "o")
    ax.set_xlabel("Cluster size, nm")

    out_name = Path("experiments/figures/figure_1.svg")
    plt.savefig(out_name)


if __name__ == "__main__":
    main()
