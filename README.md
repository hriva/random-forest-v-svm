# Overview of simple Random Forest vs Suport Vector Machine.

> DISCLAIMER: This script is for demonstrative propouses only and should not be used as is in production.

# Objective

The propose of this repository is to showcase the implementation of code for text classification methods. **Hyperparameter tunning, data augmentation and other methods** are not in the scope.

In the code are mentioned decisions made through the process but they do not dig into the statistical or mathematical backgrounds.

## Requirements

This project requires Python <= 3.12. I recommed to make a virtual enviorment to test it.

## Test a Model Release

1.  Clone the repo
```sh
git clone https://github.com/hriva/random-forest-v-svm.git
cd random-forest-v-svm

# Make virt-env
python3 -m venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Download one of the [pre-trained models](https://github.com/hriva/random-forest-v-svm/releases/latest)

3. Run the test_mail.ipynb Notebook


## Train the Model with Notebook

1.  Clone the repo
```sh
git clone https://github.com/hriva/random-forest-v-svm.git
cd random-forest-v-svm

# Make virt-env
python3 -m venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Download the data set (not in this repo) to the working directory.
> Yout need a kaggle account to download the data set.
https://www.kaggle.com/datasets/subhajournal/phishingemails/download?datasetVersionNumber=1

4. Unzip the dataset.
```sh
# this creates a directory and extracts there.
unzip archive.zip -d data
```

5. Run the notebook.

## Train the Model with Web Interface

1.  Clone the repo
```sh
git clone https://github.com/hriva/random-forest-v-svm.git
cd random-forest-v-svm

# Make virt-env
python3 -m venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Start the web Interface

```sh
streamlit run app.py
```

3. Download the data set (not in this repo) to the working directory.
> Yout need a kaggle account to download the data set.
https://www.kaggle.com/datasets/subhajournal/phishingemails/download?datasetVersionNumber=1

4. Unzip the dataset.
```sh
# this creates a directory and extracts there.
unzip archive.zip -d data
```

5. Open the web app url http://localhost:8501/
6. Select the csv to train the model. After the model is trained a text input will appear.
7. Enter the body of the mail you want to test in the text input.
