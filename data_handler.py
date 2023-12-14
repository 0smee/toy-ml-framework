import numpy as np
import pandas as pd

class DataHandler:

    def __init__(self, file_path):
        # initialises attributes of the class
        self.file_path = file_path
        self.data = None
        self.train_data = None
        self.test_data = None
        
    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.load_csv()
        elif self.file_path.endswith('.parquet'):
            self.load_parquet()
        elif self.file_path.endswith('.pkl'):
            self.load_pickle()
        else:
            raise ValueError("Unsupported file type")
    
    def splitting(self, test_size = 0.2):
        pass

    def preprocessing():
        pass
