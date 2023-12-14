import numpy as np
import pandas as pd
from data_handler import DataHandler

class DataPreprocessor:
    def __init__(self, data):
        self.data = data
    
    def missing_values(self, drop_rows = False, drop_cols = False):
        if drop_rows:
            self.data.dropna(axis=0, inplace=True)
        elif drop_cols:
            self.data.dropna(axis=1, inplace=True)
        else:
            for col in self.data:
                if self.data[col].dtype == "object":
                    # mode for categorical
                    mode_value = self.data[col].mode()[0]
                    self.data[col].fillna(mode_value, inplace=True)
                elif np.issubdtype(self.data[col].dtype, np.datetime64):
                    # forward fill for datetime
                    self.data[col].fillna(method='ffill', inplace=True)
                else:
                    # mean for numerical data
                    mean_value = self.data[col].mean()
                    self.data[col].fillna(mean_value, inplace=True)


    def scaling(self):
        pass

    def cat_encoding(self):
        pass

    def transform(self):
        self.missing_values()
        self.scaling()
        self.cat_encoding()

        return self.data