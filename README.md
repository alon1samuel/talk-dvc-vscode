# dvc_vscode
How to use DVC pipelines and vscode notebook extensions to run Data Science experiments in Python

## Introduction
This is a repo that was done for a lecture for PyData Bristol on 11.10.2022. 
This repo has the materials for a simple DVC pipeline and how to monitor results using
VSCode notebook extension - check changes.

## How to visualise the pipeline

You can explore the pipeline in the [dvc.yaml](./dvc.yaml). 
To generate the graph visualization above, run: 

`poetry run dvc dag --dot | dot -Tpng > dag.png`

## Prerequists
1. [Poetry](https://python-poetry.org/).
2. [Graphviz](https://graphviz.org/).
3. []().

## To start

1. `git clone https://github.com/polecat-dev/dvc_vscode.git`
2. `cd dvc_vscode`
3. `poetry install` (installing dependencies)
4. `poetry shell`
4. ``
