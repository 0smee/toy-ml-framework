import pandas as pd
import numpy as np
from data_handler import DataHandler
from data_preprocessor import DataPreprocessor

# testing loading in with a csv file
csv_test = DataHandler("testfiles/NovelCoronaVirus2019Dataset/covid_19_data.csv")
csv_test.load_data()
print(csv_test.data.head())

# testing splitting of data
csv_test.splitting(test_size=0.2)
print("\nTrain sample size:")
print(csv_test.train_data.shape[0])
print("\nTest Sample size:")
print(csv_test.test_data.shape[0])

# error handling test
# empty_test = DataHandler("non_existent_file.csv")
# empty_test.splitting()

# new test data
new_test_data = DataHandler("testfiles/sample_data.csv")
new_test_data.load_data()

# splitting
new_test_data.splitting(test_size=0.2)
print("\nTrain sample size:")
print(new_test_data.train_data.shape[0])
print("\nTrain sample:")
print(new_test_data.train_data.head())

# instansiate preprocessors
train_preprocessor = DataPreprocessor(new_test_data.train_data)
# not so sure about this
test_preprocessor = DataPreprocessor(new_test_data.test_data)

preprocessed_train_data = train_preprocessor.transform()
preprocessed_test_data = test_preprocessor.transform()

print("\nPreprocessed Train Data Shape:")
print(preprocessed_train_data.shape)
print("\nPreprocessed Train Data Sample:")
print(preprocessed_train_data.head())

print("\nPreprocessed Test Data Shape:")
print(preprocessed_test_data.shape)
