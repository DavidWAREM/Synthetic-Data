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
            try:
                # Accessing the first column by name
                value = row['LEI']
                logging.debug(f"Original value at index {idx}, column LEI: {value}")

                # Check if the value can be converted to float
                try:
                    float_value = float(value)
                except ValueError:
                    logging.debug(f"Value at index {idx}, column LEI is not a float: {value}")
                    continue  # Skip to the next row if value cannot be converted

                # Convert the value to float before multiplication
                new_value = float_value * random.uniform(0.3, 3)
                self.dataframe.at[idx, 'LEI'] = new_value
                logging.debug(f"New value at index {idx}, column LEI: {new_value}")
            except KeyError as e:
                logging.error(f"Column LEI not found in DataFrame")
            except ValueError as e:
                logging.error(f"Cannot convert value to float at index {idx} in column LEI: {e}")

    def write_dataframe_as_txt(self, i):
        """
        Writes the given DataFrame to a new text file with an incremented counter 'i' at the end of the file name.
        """
        # Extract directory and original file name
        directory, original_file_name = os.path.split(self.original_file_path)
        file_name, file_extension = os.path.splitext(original_file_name)

        # Create new file name with counter 'i'
        new_file_name = f"{file_name}_{i}{file_extension}"
        new_file_path = os.path.join(directory, new_file_name)

        logging.info(f"Writing DataFrame to new file: {new_file_path}")
        try:
            self.dataframe.to_csv(new_file_path, index=False, header=False, sep=';')
            logging.debug("DataFrame written to file successfully")
        except Exception as e:
            logging.error(f"An error occurred while writing to file: {e}")


# Example usage
if __name__ == "__main__":
    from data_loader import DataLoader

    file_path = "C:\\Users\\d.muehlfeld\\weitere Daten\\14_Spechbach_RNAB.TXT"
    data_loader = DataLoader(file_path)
    df = data_loader.read_txt()

    if df is not None:
        data_processor = DataProcessor(df, file_path)
        data_processor.change_friction()
        counter = 1  # You can change this to any integer value
        data_processor.write_dataframe_as_txt(counter)
