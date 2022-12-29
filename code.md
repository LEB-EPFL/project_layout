# Code and Scripting Guidelines

## Use Conda to manage environments

Conda is an environment manager and, contrary to popular belief, is intended to manage more than just Python packages. (In fact, it can be used to install packages and versions of other programming languages, such as `R`.) It can install math libraries, programming languages, and packages all into one environment.

When in doubt, use Conda (preferrably Miniconda) to manage a programming environment for a project. You can use other environment managers if they better suit your needs.

### Use Conda environment files instead of installing packages manually

A Conda environment file contains a specification for a Conda environment. You can install a new environment directly from the file with the command `conda env create -f environment.yml`.

An example environment file looks like the following:

```
name: rl-storm
channels:
  - conda-forge
  - defaults
  - pytorch
dependencies:
  - jupyter
  - matplotlib
  - conda-forge::stackview
  - numpy
  - pip
  - pip:                                
    - gymnasium
    - pygame                                                
    - git+ssh://git@github.com/LEB-EPFL/imajin.git
    - git+ssh://git@github.com/LEB-EPFL/imajin-kit.git#egg=leb-imajin-kit-learn&subdirectory=learn
  - python=3.10
  - pytorch::pytorch
  - pytorch::torchvision
```

The above will create an environment named `rl-storm`. It will pull packages from `conda-forge` first, followed by `defaults` and `pytorch` if the packages do not exist on `conda-forge`. The environment will use Python 3.10. Four packages (`gymnasium`, `pygame`, and two GitHub repos) will be installed using `pip` and not Conda. Finally, `pytorch` and `torchvision` will be installed from the `pytorch` channel.

### Use the `conda-forge` channel

Packages in the `defaults` channel are often very out-of-date. Use `conda-forge` instead to get up-to-date packages.

For example: `conda install -c conda-forge scikit-learn`

## Prefer open-source software where possible and convenient

Open-source software should be preferred because it improves the chances of a work's reproduction by others.

In some cases, closed-source software can be used when there are no easy-to-use alteratives or well-accepted alternatives, such as using Labview for FPGA programming.

## Paths and file locations in scripts

All scripts and notebooks should assume that they are being run from the root project folder. For example, if your analysis script requires a file `data/experiment_1/my_data.txt`, then the script should use this relative path to the file and not refer to an absolute path.

This guideline helps to ensure that all scripts can run independently of a specific person's file system. A script that tries to load the file `D:\Users\JaneDoe\my-kewl-datazzz\cats.jpg` is unlikely to run without modification on anyone's computer except for Jane's. Instead, the script should load `data\experiment_1\cats.jpg`.

This guideline requires that the project root is in your `PATH` environment variable in your programming language's interpreter. In Python, for example, the folder from which the `python` command is executed is automatically added to `sys.path`. So if your Python code looks like the following, then it should work so long as you launched Python from this directory:

```python
filename = "data/experiment_1/data.csv"
with open(filename, "r") as f:
    # Do stuff here...
```

## Projects that are code only can go in their own repository

If you have a project that is ONLY code, such as a library or tool, put it in its own repository. This makes it easier to re-use in multiple projects.