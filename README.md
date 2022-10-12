# dvc_vscode
How to use DVC pipelines and vscode notebook extensions to run Data Science experiments in Python

## Introduction
This is a repo that was done for a lecture for PyData Bristol on 11.10.2022. 

This repo has the materials for a simple DVC pipeline and how to monitor results using
VSCode notebook extension - check changes.

Lecture link - TBC

## Prerequists
1. [Poetry](https://python-poetry.org/).
2. [Graphviz](https://graphviz.org/).
3. [VSCode](https://code.visualstudio.com/).

## Installation (on linux)

`git clone https://github.com/polecat-dev/dvc_vscode.git`

`cd dvc_vscode`

`poetry install` (installing dependencies)

`poetry shell`

`python scripts/init_files.py`

## To start

To reproduce the pipeline - 

`dvc repro`

To visualise results - 

Go to [results](notebooks/results.ipynb).

Define your kernel (with the poetry virtualenv).

Run all cells.

Save notebook changes.

Go to source control VSCode extension to check results changes.


## How to visualise the pipeline

You can explore the pipeline in the [dvc.yaml](./dvc.yaml). 
To generate the graph visualization above, run: 

`poetry run dvc dag --dot | dot -Tpng > dag.png`

![dag-image](dag.png)
## Credits
Thanks to [PyData Bristol](https://github.com/pydatabristol) for the talk opportunity.

Thanks to [Polecat](https://www.polecat.com/) for the time and information sharing.

Thanks to [SpaCy](https://github.com/explosion/projects/tree/v3/tutorials/textcat_docs_issues) for the materials.

Thanks to [DVC](https://github.com/iterative/dvc).


Maintainer - [Alon Samuel](https://github.com/alon1samuel).
