# Project Layout

Template for research project folders in the [Laboratory of Experimental Biophysics](https://www.epfl.ch/labs/leb/).

## How to use this template

This template may be used in the following ways when starting a new project in the LEB:

- Create a new GitHub repository by clicking the `Use this template` button above, then cloning the resulting repo to your local machine
- Clone the repo by clicking the `Code` button above
- Download the repo by clicking the `Code` button above and unzip it to a directory of your choosing
- Manually create the folders and files on your own in a way that mimics this repo

If you are uncertain, then do not hesitate to ask :D

## Data flow

In general, data flows through a project by passing through the following folders:

```mermaid
flowchart TD
    data --> experiments/exploration
    data --> experiments/analysis
    experiments/analysis --> experiments/figures 
    
```

Raw data is stored in the [data](data) folder. Next, scripts in the [experiments/exploration](experiments/exploration) folder are used for intial data exploration and visualization. Once an analysis is ready to be finalized, scripts in the [experiments/analysis](experiments/analysis) folder perform the analysis. Intermediate results are also stored there. Finally, figures are created from the intermediate results by scripts in the [experiments/figures](experiments/figures) folder.

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

### [sandbox](sandbox)

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

### Code

Guidelines for organizing and running code are in the file [code.md](code.md).

### Filenames

See [filenames.md](filenames.md) for more information about how to name files.

### Date format

See [dates.md](dates.md).

### Publication

See [publications.md](publications.md).

## Additional Resources

- [Ten Simple Rules for Digital Data Storage](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005097)

## Acknowledgements

This template was inspired by the following resources:

- [gchure/reproducible_research](https://github.com/gchure/reproducible_research)
