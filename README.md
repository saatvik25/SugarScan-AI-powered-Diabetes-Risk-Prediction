# SugarScan-AI-powered-Diabetes-Risk-Prediction
This repository contains code and data for a diabetes prediction project using machine learning techniques. The project involves predicting whether an individual has diabetes based on various health-related features.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Data](#data)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this project, we aim to predict the likelihood of diabetes in individuals based on their health attributes such as age, gender, hypertension, heart disease, smoking history, BMI, HbA1c level, and blood glucose level. We utilize the K-nearest neighbors (KNN) algorithm for the predictive task.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt`.

## Data

The dataset used for this project is stored in the file `diabetes_prediction_dataset.csv`. It contains various attributes related to health and diabetes status.

## Data Preprocessing

Data preprocessing is a crucial step in any machine learning project. In this project, we perform the following preprocessing steps:
- Handling missing values
- Encoding categorical variables using label encoding

## Model Training

We train a K-nearest neighbors (KNN) classifier using the preprocessed data. The model is trained to predict diabetes status based on the input features.

## Model Evaluation

The model's performance is evaluated using various metrics such as accuracy, precision, recall, and F1-score. The trained model is saved as a pickle file for future use.

## Usage

To use the trained model for predicting diabetes status, follow these steps:

1. Load the trained model using `pickle`:
   ```python
   import pickle

   with open('model.pkl', 'rb') as file:
       model = pickle.load(file)
