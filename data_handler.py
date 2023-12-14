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
        try:
            if self.file_path.endswith('.csv'):
                self.data = pd.read_csv(self.file_path)
            elif self.file_path.endswith('.parquet'):
                self.data = pd.read_parquet(self.file_path)
            elif self.file_path.endswith('.pkl'):
                self.data = pd.read_pickle(self.file_path)
            else:
                raise ValueError("Unsupported file type")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except pd.errors.ParserError:
            print(f"Error parsing file: {self.file_path}")
        except Exception as ex:
            print(f"An error occurred: {ex}")


    def splitting(self, test_size = 0.2):
        if self.data is None or self.data.empty:
            print("No data loaded to split.")
            return
        train_size = 1-test_size
        # shuffle index of data
        shuffled_indices = self.data.index.to_numpy()
        np.random.shuffle(shuffled_indices)
        # calculate index for splitting
        split_index = int(train_size * len(shuffled_indices))
        # splitting the data and saving 
        self.train_data = self.data.loc[shuffled_indices[:split_index]]
        self.test_data = self.data.loc[shuffled_indices[split_index:]]
    
    
    def preprocessing():
        pass
