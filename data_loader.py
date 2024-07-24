import pandas as pd
import logging
import os

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class DataLoader:
    def __init__(self, file_path):
        """
        Initializes the DataLoader with the path to the text file.
        """
        self.file_path = file_path
        self.dataframe = None  # Initialize the DataFrame as None
        logging.info(f"DataLoader initialized with file path: {file_path}")

    def read_txt(self):
        """
        Reads a text file, parses its content into a DataFrame, and returns it.
        """
        logging.info(f"Attempting to read file: {self.file_path}")
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                logging.debug("File opened successfully")
                data = file.read()
                logging.debug("File read into memory")

                from io import StringIO
                self.dataframe = pd.read_csv(StringIO(data), delimiter=';', header=None)
                logging.debug("Data parsed into DataFrame")

                # Add column names if not present
                self.dataframe.columns = ['ANF', 'END', 'RAU']

                return self.dataframe

        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            return None
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return None
