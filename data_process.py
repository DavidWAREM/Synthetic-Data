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
        logging.info("Starting to change friction values for rows where the first column is 'RAU'.")
        # Create a copy of the original dataframe
        modified_dataframe = self.dataframe.copy()

        for idx, row in modified_dataframe.iterrows():
            try:
                # Accessing the first column by name
                value = row['RAU']
                logging.debug(f"Original value at index {idx}, column RAU: {value}")

                # Check if the value can be converted to float
                try:
                    float_value = float(value)
                except ValueError:
                    logging.debug(f"Value at index {idx}, column RAU is not a float: {value}")
                    continue  # Skip to the next row if value cannot be converted

                # Convert the value to float before multiplication
                new_value = float_value * random.uniform(0.3, 3)
                modified_dataframe.at[idx, 'RAU'] = new_value
                logging.debug(f"New value at index {idx}, column RAU: {new_value}")
            except KeyError as e:
                logging.error(f"Column RAU not found in DataFrame")
            except ValueError as e:
                logging.error(f"Cannot convert value to float at index {idx} in column RAU: {e}")

        return modified_dataframe

    def write_dataframe_as_txt(self, dataframe, i):
        """
        Writes the given DataFrame to a new text file with an incremented counter 'i' at the end of the file name.
        """
        # Extract directory and original file name
        directory, original_file_name = os.path.split(self.original_file_path)
        synthetic_data_dir = os.path.join(directory, "Synthetic_Data")

        # Create Synthetic_Data directory if it doesn't exist
        os.makedirs(synthetic_data_dir, exist_ok=True)

        # Create new file name with counter 'i'
        file_name, file_extension = os.path.splitext(original_file_name)
        new_file_name = f"{file_name}_{i}.txt"  # Ensure the extension is .txt
        new_file_path = os.path.join(synthetic_data_dir, new_file_name)

        logging.info(f"Writing modified DataFrame to new file: {new_file_path}")
        try:
            dataframe.to_csv(new_file_path, index=False, header=False, sep=';')
            logging.debug("DataFrame written to file successfully")
        except Exception as e:
            logging.error(f"An error occurred while writing to file: {e}")
