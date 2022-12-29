# Preparing a project folder for publication

When it comes time to publish a manuscript, we will often want to place all the data, scripts, and resources that accompany the manuscript in an online repository, such as Zenodo. This is probably going to require a bit more work than simply zipping the project folder and uploading it since it will likely contain files that should not be included, such as previous submissions or personal communications.

This guide should help you therefore to prepare a project folder for archival once a project is submitted.

## What not to include

Everything in a project folder should be included for archival and public release except for the following:

- The entire `sandbox` folder
- Any reports in the `reports` folder that are not related to the publication. This includes, for example, previous submissions to other journals. Preprints are OK to include.
- Data in the `data` folder that is not used in the manuscript
- The `.git` folder if it exists. This is the git database with the version history of all the files. If you release the project as a GitHub repository, then you won't need to worry about this; the GitHub repository will have the project's entire history. If you're not certain about this part, then don't hesitate to ask someone in the lab.
- Any figures in `experiments/figures` that aren't in the manuscript. Figures from exploratory analyses are OK to include, but these ought to go in the `experiments/exploration` folder.

The preferred way to remove any files before publication is to copy the whole project folder and delete the unneeded files from the copy.
