"""This is a fake script. It only serves to illustrate how one might read data and analyze it.

Run the script from the project root directory:

```
python experiments/analysis/2023-04-17-hela-trf2-clustering/cluster.py
```

"""

from pathlib import Path

import numpy as np


def cluster_sizes(data: np.ndarray) -> np.ndarray:
    """Clusters localizations in a Nx3 data and computes their sizes.

    data: a Nx3 array of x,y,z localizations.
    returns: a Mx1 array of cluster sizes, where M is the number of clusters.
    
    This is a fake function for illustrative purposes only! Fake results are returned.

    """
    # do cluster size analysis here

    return np.array([52.3, 77.5, 67.2, 88.4, 75.3])


def main():
    # Paths are relative to the project root directory by convention!
    fname = Path("data/2023-04-17-hela-trf2-knockdowns/fov_1_localizations.csv")
    data = np.genfromtxt(fname, delimiter=",", skip_header=1)

    # Compute cluster sizes
    sizes = cluster_sizes(data)

    # Save sizes to a file
    out_name = Path("experiments/analysis/2023-04-17-hela-trf2-clustering/results.csv")
    np.savetxt(out_name, sizes, delimiter=",")


if __name__ == "__main__":
    main()
