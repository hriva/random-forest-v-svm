# Overview of simple Random Forest vs Suport Vector Machine.

> DISCLAIMER: This script is for demonstrative propouses only and should not be used as is in production.

# Objective

The propose of this repository is to showcase the implementation of code for text classification methods. **Hyperparameter tunning, data augmentation and other methods** are not in the scope.

In the code are mentioned decisions made through the process but they do not dig into the statistical or mathematical backgrounds. 

## Requirements

This project requires Python <= 3.12. I recommed to make a virtual enviorment to test it.

### Clone the repo
```sh
git clone https://github.com/hriva/random-forest-v-svm.git
cd random-forest-v-svm

# Make virt-env
python3 -m venv 
./.venv/bin/activate
pip install -r requirements.txt
```
## Running the Project

1. Download the data set (not in this repo).
> Yout need a kaggle account to download the data set.  
https://www.kaggle.com/datasets/subhajournal/phishingemails/download?datasetVersionNumber=1

3. Unzip the dataset.
```sh
# this creates a directory and extracts there.
unzip archive.zip -d data
```

2. Run the notebook.

