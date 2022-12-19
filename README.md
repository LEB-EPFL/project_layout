# Project Layout

Template for research project folders in the [Laboratory of Experimental Biophysics](https://www.epfl.ch/labs/leb/).

## How to use this template

TODO

## Layout

The following folders in this layout are mandatory unless you do not yet have contents for any of them. In this case, the folders may either be empty or simply not present. This is expected in the early days of a project when you may not yet have, for example, any reports or well-established templates.

Each folder in this list should contain a README.md that provides an overview of its contents.

### [data](data)

The [data](data) folder contains all raw data from your experiments.

### [experiments](experiments)

The [experiments](experiments) folder contains exploration, processing, and analysis scripts, as well as files containing data in an intermediate format.

- [analysis](experiments/analysis) contains scripts and notebooks that derive conclusions from data, including figures that are just for understanding an experiment. Statistical analyses, calculations, regressions, etc. go here.
- [exploration](experiments/exploration) contains scripts and notebooks for trying different types of analysis and visualizations. Often your first scripts will go here because will not yet know what works and what doesn't.
- [figures](experiments/figures) contains scripts that generate final figures for presentations, publication, etc.

Processing data into an intermediate form may go in analysis as well.

### [misc](misc)

This folder contains all files that are **not** data, code, or the result of analyses such as figures or texts. Examples include:

- protocols
- materials
- notes
- communications between collaborators

Files in this folder will be included with the dataset in any final publication.

### [modules](modules)

The [modules](modules) folder contains reusable source code for your project. It may be, for example, a Python package, or it could be just a list files containing functions to use in your analysis.

The difference between code in the `modules` directory and the `experiments` directory is that code in this directory is intended to be reused multiple times. For example if you have a function that cleans up many different datasets, you should put the function in a file in this folder and import it in your analysis.

### [reports](reports)

This folder contains different project reports, such as

- manuscripts submitted for publication
- preprints
- conference presentations
- group meeting presentations

### [sandox](sandbox)

This is a free-form folder that may contain anything you like. You may structure its contents however you wish. However, any files that eventually support a publication cannot be located within this folder.

### [templates](templates)

Files in this folder serve as templates for creating new files that describe, for example,

- experiments
- simulations
- protocols

## Project Master

The [project master](project_master.xlsx) is a file used to track individual contributions to a project. The purpose is to ensure that authorship on projects is handled correctly by documenting each person's contribution to a project.

A project master template is provided in this repository.

## Guidelines

### Paths and file locations in scripts

All scripts and notebooks should assume that they are being run from this root project folder. For example, if your analysis script requires a file `data/experiment_1/my_data.txt`, then the script should use this relative path to the file and not refer to an absolute path.

This guideline helps to ensure that all scripts can run independently of a specific person's file system. A script that tries to load the file `D:\Users\JaneDoe\my-kewl-datazzz\cats.jpg` is unlikely to run without modification on anyone's computer except for Jane's. Instead, the script should load `data\experiment_1\cats.jpg`.

This guideline requires that the project root is in your `PATH` environment variable in your programming language's interpreter. In Python, for example, the folder from which the `python` command is executed is automatically added to `sys.path`. So if your Python code looks like the following, then it should work so long as you launched Python from this directory:

```python
filename = "data/experiment_1/data.csv"
with open(filename, "r") as f:
    # Do stuff here...
```

### Code

Guidelines for organizing and running code are in the file [code.md](code.md).

### Filenames

See [filenames.md](filenames.md) for more information about how to name files.

### Date format

See [dates.md](dates.md).

### Publication

TODO

## Acknowledgements

This template was inspired by the following resources:

- [gchure/reproducible_research](https://github.com/gchure/reproducible_research)
