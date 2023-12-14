# Machine Learning Framework

Welcome to my Machine Learning Framework!

## Overview

This is a Python-based machine learning framework designed for data handling and preprocessing. It's a useful tool for data scientists and machine learning enthusiasts.

## Features

- Data loading from CSV, Parquet, and Pickle formats.
- Data splitting for model training and testing.
- Data preprocessing for handling missing values and scaling features.
- Practice Object-Oriented Programming (OOP) in a fun way!

## Getting Started

1. Clone this repository to your local machine:

   - ``` bash
     git clone https://github.com/your-username/ml-framework.git

2. Install the required dependencies:

   - ``` bash
     pip install -r requirements.txt
     ```

3. Start using the framework in your projects! 

   

   ## Usage:

   You can use this framework by creating instances of the `DataHandler` and `DataPreprocessor` classes. Here's an example: 

   ``` python
   #Import the classes from data_handler 
   import DataHandler from data_preprocessor import DataPreprocessor 
   # Load data 
   data_handler = DataHandler("your_dataset.csv") 
   data_handler.load_data() 
   # Split the data 
   data_handler.splitting(test_size=0.2) 
   # Preprocess the data 
   preprocessor = DataPreprocessor(data_handler.train_data) 
   preprocessed_data = preprocessor.transform() 
   # Now you're ready for machine learning!
   ```

   

   