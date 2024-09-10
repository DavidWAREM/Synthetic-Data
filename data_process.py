import pandas as pd
import logging
import random
import os


# This class is responsible for processing a pandas DataFrame and performing operations such as
# modifying the 'RAU' column values and saving the modified DataFrame as a new text file.
class DataProcessor:
    def __init__(self, dataframe, original_file_path):
        """
        Initializes the DataProcessor class.

        :param dataframe: The DataFrame that contains the data to be processed.
        :param original_file_path: The file path of the original text file, used for file saving operations.

        Attributes:
        - dataframe: Stores the provided DataFrame for further manipulation.
        - original_file_path: Stores the path to the original file, which will be used to determine the save location.

        Logs the initialization process, including the original file path.
        """
        self.dataframe = dataframe
        self.original_file_path = original_file_path
        logging.info(f"DataProcessor initialized with file: {original_file_path}")

    def change_friction(self):
        """
        Modifies the 'RAU' column values for all rows in the DataFrame. It multiplies the original value
        by a random number between 0.3 and 3, but only if the value is numeric.

        Steps:
        1. Copy the original DataFrame to preserve the original data.
        2. Iterate over each row in the DataFrame.
        3. For rows where the 'RAU' column is numeric, multiply the value by a random float between 0.3 and 3.
        4. Log the original and new values for debugging purposes.

        Returns:
        - A modified DataFrame with updated 'RAU' column values.
        """
        logging.info("Starting to change friction values for rows where the first column is 'RAU'.")

        # Create a copy of the original DataFrame to avoid changing the original data.
        modified_dataframe = self.dataframe.copy()

        # Iterate over each row in the DataFrame.
        for idx, row in modified_dataframe.iterrows():
            try:
                # Accessing the 'RAU' column in the row by column name.
                value = row['RAU']
                logging.debug(f"Original value at index {idx}, column RAU: {value}")

                # Check if the value can be converted to float (to ensure it's numeric).
                try:
                    float_value = float(value)
                except ValueError:
                    # If the value is not numeric, skip this row and move to the next.
                    logging.debug(f"Value at index {idx}, column RAU is not a float: {value}")
                    continue

                # If numeric, multiply the value by a random float between 0.3 and 3.
                new_value = float_value * random.uniform(0.3, 3)
                # Update the value in the DataFrame at the corresponding index.
                modified_dataframe.at[idx, 'RAU'] = new_value
                logging.debug(f"New value at index {idx}, column RAU: {new_value}")

            # Handle any cases where the 'RAU' column is not found in the DataFrame.
            except KeyError as e:
                logging.error(f"Column RAU not found in DataFrame")

            # Handle errors related to value conversion issues (if float conversion fails).
            except ValueError as e:
                logging.error(f"Cannot convert value to float at index {idx} in column RAU: {e}")

        return modified_dataframe

    def write_dataframe_as_txt(self, dataframe, current_number):
        """
        Writes the modified DataFrame to a new text file, appending a counter (current_number) to the file name.

        Steps:
        1. Extract the directory and original file name from the original file path.
        2. Create a new directory called 'Synthetic_Data' inside the original file's directory.
        3. Generate a new file name by appending the current_number to the original file name.
        4. Save the modified DataFrame as a text file (.txt) in the 'Synthetic_Data' directory.

        :param dataframe: The DataFrame to be written to the file.
        :param current_number: An integer that will be appended to the file name for uniqueness.
        """
        # Extract the directory path and the original file name.
        directory, original_file_name = os.path.split(self.original_file_path)
        synthetic_data_dir = os.path.join(directory, "Import Data")

        # Create the 'Synthetic_Data' directory if it doesn't already exist.
        os.makedirs(synthetic_data_dir, exist_ok=True)

        # Split the original file name into name and extension, then append current_number to create a new name.
        file_name, file_extension = os.path.splitext(original_file_name)
        new_file_name = f"{file_name}_{current_number}.txt"  # Ensure the new file has a .txt extension.
        new_file_path = os.path.join(synthetic_data_dir, new_file_name)

        logging.info(f"Writing modified DataFrame to new file: {new_file_path}")

        try:
            # Write the DataFrame to a new text file, with no header and using ';' as the delimiter.
            dataframe.to_csv(new_file_path, index=False, header=False, sep=';')
            logging.debug("DataFrame written to file successfully")

        # Catch any errors that occur during the file writing process and log them.
        except Exception as e:
            logging.error(f"An error occurred while writing to file: {e}")
