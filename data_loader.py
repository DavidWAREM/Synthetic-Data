import pandas as pd
import logging
import os

# Set up logging configuration to capture detailed logs.
# Logs will show the time, log level (INFO, DEBUG, ERROR), and the log message.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class DataLoader:
    def __init__(self, file_path):
        """
        Initializes the DataLoader class with the given file path.

        Parameters:
        - file_path (str): The path to the text file that needs to be loaded.

        Attributes:
        - file_path (str): Stores the path of the file to be read.
        - dataframe (pandas.DataFrame): Initially set to None; will store the loaded data later as a DataFrame.

        Logging is set up to capture when the DataLoader is initialized.
        """
        self.file_path = file_path
        self.dataframe = None  # Initialize the DataFrame as None (no data loaded yet).
        logging.info(f"DataLoader initialized with file path: {file_path}")

    def read_txt(self):
        """
        Reads the text file located at the file path, parses its content, and loads it into a pandas DataFrame.

        Steps:
        1. Open the file at the specified path.
        2. Read the content of the file.
        3. Parse the content using pandas `read_csv` with a custom delimiter (`;`) to create a DataFrame.
        4. Assign column names if not already present in the data.

        Returns:
        - A pandas DataFrame containing the file data (if read successfully).
        - If an error occurs (like FileNotFoundError), the function returns None and logs the error.

        Logs provide details about the success or failure of file reading and parsing.
        """
        logging.info(f"Attempting to read file: {self.file_path}")
        try:
            # Open the file with UTF-8 encoding in read mode
            with open(self.file_path, 'r', encoding='utf-8') as file:
                logging.debug("File opened successfully")  # Log when file is successfully opened.

                # Read the file contents into memory
                data = file.read()
                logging.debug("File read into memory")  # Log after reading the file.

                # Using StringIO to treat the string data as a file-like object for pandas to read
                from io import StringIO
                self.dataframe = pd.read_csv(StringIO(data), delimiter=';', header=None)
                logging.debug("Data parsed into DataFrame")  # Log when data is successfully parsed into a DataFrame.

                # Assign column names to the DataFrame (if needed)
                self.dataframe.columns = ['STANET-ID', 'RAU']

                return self.dataframe

        # Error handling for when the file is not found.
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")  # Log file not found error.
            return None

        # Catch any other exceptions, log the error, and return None.
        except Exception as e:
            logging.error(f"An error occurred: {e}")  # Log any other types of errors that might occur.
            return None
