import pandas as pd
import logging
import random
import os

# Updated value series
value_series = [
    "LEI0000B562FD357EF45E_2",
    "LEI0000B362FD357EF3A9",
    "LEI0000B462FD357EF3E4_1",
    "LEI0000CF62FD357EFA58_2",
    "LEI0000D262FD357EFB42",
    "LEI00004662FD357EDEF7",
    "LEI00004562FD357EDEB3",
    "LEI0000D162FD357EFAE0",
    "LEI0000D062FD357EFA97",
    "LEI00004862FD357EDF90",
    "LEI00005B62FD357EE44A",
    "LEI0000E562FD357EFE28",
    "LEI0000E662FD357EFE74",
    "LEI0000FD62FD357E03A8_1",
    "LEI00008862FD357EEAD8_1",
    "LEI00008B62FD357EEB84",
    "LEI00000362FD357ED32A",
    "LEI00000762FD357ED46F",
    "LEI00000862FD357ED4AE",
    "LEI00007462FD357EE818",
    "LEI00007562FD357EE839",
    "LEI0000FF62FD357E049F",
    "LEI0000C262FD357EF79A_2",
    "LEI00000662FD357ED41C",
    "LEI00010962FD357E0795",
    "LEI00003B62FD357EDC81",
    "LEI00001562FD357ED7C6_1",
    "LEI00009E62FD357EEF5F_2",
    "LEI00006F62FD357EE6A3_1",
    "LEI00010862FD357E06C4_2",
    "LEI00009362FD357EECE3_1",
    "LEI00004962FD357EDFD4_1",
    "LEI000172637CA74B5A6E",
    "LEI0000CD62FD357EF9D9_2",
    "LEI0000A162FD357EF008",
    "LEI0000F962FD357E015D",
    "LEI00005A62FD357EE2C9_1"
]


# This class is responsible for processing a pandas DataFrame and performing operations such as
# modifying the last value in the third row and saving the modified DataFrame as a new text file.
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

    def change_last_value(self):
        """
        Modifies the last value in the third row of the DataFrame with a random value from the provided value series.

        Steps:
        1. Ensure the DataFrame has at least three rows.
        2. Replace the last value of the third row with a random choice from the value series list.

        Returns:
        - A modified DataFrame with the updated third row's last value.
        """
        logging.info("Starting to change the last value in the third row of the DataFrame.")

        # Ensure the DataFrame has at least three rows.
        if len(self.dataframe) > 2:
            # Replace the last value of the third row with a random value from the value series list.
            random_value = random.choice(value_series)
            self.dataframe.iloc[2, -1] = random_value
            logging.debug(f"Last value in the third row updated to: {random_value}")
        else:
            logging.warning("DataFrame has less than three rows; no changes made.")

        return self.dataframe

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


def main():
    input_file = 'input.csv'  # Path to the input file
    output_counter = 1  # Counter for the output file

    # Read the DataFrame
    dataframe = pd.read_csv(input_file)
    processor = DataProcessor(dataframe, input_file)

    # Change the last value of the third row
    modified_dataframe = processor.change_last_value()

    # Write the DataFrame to a text file
    processor.write_dataframe_as_txt(modified_dataframe, output_counter)


if __name__ == "__main__":
    main()