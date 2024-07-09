import pandas as pd
import logging
import random
import os

class DataProcessor:
    def __init__(self, dataframe, original_file_path):
        """
        :param dataframe: The DataFrame to process
        :param original_file_path: The path to the original file
        """
        self.dataframe = dataframe
        self.original_file_path = original_file_path
        logging.info(f"DataProcessor initialized with file: {original_file_path}")

    def change_friction(self):
        logging.info("Starting to change friction values for rows where the first column is 'LEI'.")
        for idx, row in self.dataframe.iterrows():
            if row.iloc[0] == 'LEI':
                try:
                    # Accessing the column by name
                    column_name = row.index[7]
                    value = self.dataframe.at[idx, column_name]
                    logging.debug(f"Original value at index {idx}, column {column_name}: {value}")
                    # Convert the value to float before multiplication
                    value = float(value)
                    new_value = value * random.uniform(0.3, 3)
                    self.dataframe.at[idx, column_name] = new_value
                    logging.debug(f"New value at index {idx}, column {column_name}: {new_value}")
                except KeyError as e:
                    logging.error(f"Column {row.index[7]} not found in DataFrame")
                except ValueError as e:
                    logging.error(f"Cannot convert value to float at index {idx} in column {column_name}: {e}")

        # Define the directory and file name for saving the CSV
        directory = "C:\\Users\\d.muehlfeld\\weitere Daten"
        file_name = "test.csv"
        full_path = os.path.join(directory, file_name)
        logging.info(f"Saving modified DataFrame to {full_path}")
        self.dataframe.to_csv(full_path, index=False, sep=";")
        logging.info("DataFrame saved successfully.")
        return self.dataframe



# Define the directory and file path for loading the CSV
file_path = "C:\\Users\\d.muehlfeld\\weitere Daten\\Leitungen.CSV"
file_name
logging.info(f"Loading data from {file_path}")
data = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')
logging.info("Data loaded successfully.")
test = DataProcessor(data, file_path)
test.change_friction()
