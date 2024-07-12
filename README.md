# HopSkipDrive Technical Assessment
This repository contains a completed technical assessment for HopSkipDrive. It consists of Jupyter notebooks for exploratory analysis and model development, as well as source code for model data processing.

The final summary documentation can be found [here](documentation.md). For a more complete view, see the [exploratory analysis](notebooks/01_exploratory_analysis.ipynb) and [model development](notebooks/02_model.ipynb) notebooks.

## Requirements
The project uses Python 3.9. 

Requirements are listed in requirements.txt.

__Create and activate virtual environment__
```bash
python -m venv env # Replace 'env' with preferred location
source env/bin/activate
```

__Install requirements__

```bash
pip install -r requirements.txt
```

__Generate model data__

```bash
python src/process_data.py
```