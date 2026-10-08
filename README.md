# Machine Learning for Factor Investing

This repository contains a complementary Python implementation of the book *Machine Learning for Factor Investing*. While the core material follows the book, I also include extensions such as feature engineering techniques, code, topics, optimization routines, diagnostics, new algorithms, etc.

The original material and Python code associated with the book are available at:
https://www.mlfactor.com/python.html

## Data

The main dataset used throughout the project is based on `data_ml.RData`, available from the original repository:
https://github.com/shokru/mlfactor.github.io/tree/master/material

To reproduce the project:

1. Download `data_ml.RData` from the link above.
2. Extract/load the dataset.
3. Save the resulting data as:

   `data/data_ml.csv`

The CSV file is not included in this repository and should be generated locally.

## Implementation specifics

* notebook/1_prior contains code of chapters 1,3 and 4. I closely follow the original implementation, diverging only in exercise solution + code simplification.
* notebook/5_penalizedregregressions implements chapter 5. 
   * MLF_5_book - book implementation. Additionally, I provide train-val-test implementation using optuna for ElasticNet
   * MLF_5_ex - book exercise, very simple
   * MLF_5_mine - walk forward bayesian optimization for ElasticNet, less features and stocks for training purposes.


