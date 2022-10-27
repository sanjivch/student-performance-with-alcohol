# student-performance-with-alcohol
This project is part of the ML Zoomcamp 2022 Cohort. This analyses the students performance post alcohol consumption. Social, gender and study data from secondary school students.
The data were obtained in a survey of students math and portuguese language courses in secondary school. It contains a lot of interesting social, gender and study information about students. We will explore the datasets and predict students final grade based on the available data.


# Data
 The data is taken from the kaggle competition. 
  From the kaggle page,
  > The data were obtained in a survey of students math and portuguese language courses in secondary school. It contains a lot of interesting social, gender and study information about students. You can use it for some EDA or try to predict students final grade.

## Description

Deliverables
For a project, you repository/folder should contain the following:

README.md with
Description of the problem
Instructions on how to run the project
Data
You should either commit the dataset you used or have clear instructions how to download the dataset
Notebook (suggested name - notebook.ipynb) with
Data preparation and data clearning
EDA, feature importance analysis
Model selection process and parameter tuning
Script train.py (suggested name)
Training the final model
Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
Script predict.py (suggested name)
Loading the model
Serving it via a web serice (with Flask or specialized sofware - BentoML, KServe, etc)
Files with dependencies
Pipenv and Pipenv.lock if you use Pipenv
bentofile.yaml if you use BentoML
or equivalents: conda environment file, requirements.txt or pyproject.toml
Dockerfile for running the service
Deployment
URL to the service you deployed or
Video or image of how you interact with the deployed service

## How to run?
1. Run the docker

# Source Information
```P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto, Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7.

Fabio Pagnotta, Hossain Mohammad Amran.
Email:fabio.pagnotta@studenti.unicam.it, mohammadamra.hossain '@' studenti.unicam.it
University Of Camerino
```
https://archive.ics.uci.edu/ml/datasets/STUDENT+ALCOHOL+CONSUMPTION