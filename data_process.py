import pandas as pd
import logging
import random
import os

# Updated value series
value_series = [
    "LEI00000162FD357ECA6F", "LEI00000262FD357ED282", "LEI00000362FD357ED32A", "LEI00000462FD357ED39E", "LEI00000562FD357ED3D3",
    "LEI00000662FD357ED41C", "LEI00000762FD357ED46F", "LEI00000862FD357ED4AE", "LEI00000962FD357ED4F2", "LEI00000A62FD357ED526",
    "LEI00000B62FD357ED596", "LEI00000C62FD357ED5B3", "LEI00000D62FD357ED5DD", "LEI00000E62FD357ED632", "LEI00000F62FD357ED644",
    "LEI00001062FD357ED650", "LEI00001162FD357ED66D", "LEI00001262FD357ED6A3", "LEI00001362FD357ED6BA", "LEI00001462FD357ED6D3",
    "LEI00001562FD357ED7C6", "LEI00001662FD357ED7F6", "LEI00001762FD357ED851", "LEI00001862FD357ED893", "LEI00001962FD357ED89F",
    "LEI00001A62FD357ED8AA", "LEI00001B62FD357ED8BE", "LEI00001C62FD357ED8CE", "LEI00001D62FD357ED8E0", "LEI00001E62FD357ED8F0",
    "LEI00001F62FD357ED8FC", "LEI00002062FD357ED912", "LEI00002162FD357ED934", "LEI00002262FD357ED946", "LEI00002362FD357ED955",
    "LEI00002462FD357ED991", "LEI00002562FD357ED9B8", "LEI00002662FD357ED9C4", "LEI00002762FD357ED9D0", "LEI00002862FD357ED9DB",
    "LEI00002962FD357ED9E7", "LEI00002A62FD357ED9F2", "LEI00002B62FD357EDA05", "LEI00002C62FD357EDA23", "LEI00002D62FD357EDA3A",
    "LEI00002E62FD357EDA82", "LEI00002F62FD357EDAD5", "LEI00003062FD357EDB06", "LEI00003162FD357EDB29", "LEI00003262FD357EDB3A",
    "LEI00003362FD357EDB5B", "LEI00003462FD357EDB7C", "LEI00003562FD357EDB8D", "LEI00003662FD357EDBBC", "LEI00003762FD357EDBD6",
    "LEI00003862FD357EDBE9", "LEI00003962FD357EDC4B", "LEI00003A62FD357EDC5C", "LEI00003B62FD357EDC81", "LEI00003C62FD357EDCBB",
    "LEI00003D62FD357EDCF5", "LEI00003E62FD357EDD15", "LEI00004062FD357EDD76", "LEI00004262FD357EDE08", "LEI00004362FD357EDE1F",
    "LEI00004462FD357EDE4D", "LEI00004562FD357EDEB3", "LEI00004662FD357EDEF7", "LEI00004762FD357EDF3B", "LEI00004862FD357EDF90",
    "LEI00004962FD357EDFD4", "LEI00004A62FD357EE064", "LEI00004B62FD357EE089", "LEI00004C62FD357EE0B1", "LEI00004D62FD357EE0C9",
    "LEI00004E62FD357EE0D9", "LEI00004F62FD357EE0EB", "LEI00005062FD357EE100", "LEI00005162FD357EE122", "LEI00005262FD357EE157",
    "LEI00005362FD357EE168", "LEI00005462FD357EE17D", "LEI00005562FD357EE18F", "LEI00005662FD357EE1C5", "LEI00005762FD357EE20F",
    "LEI00005862FD357EE244", "LEI00005962FD357EE289", "LEI00005A62FD357EE2C9", "LEI00005B62FD357EE44A", "LEI00005C62FD357EE4D2",
    "LEI00005D62FD357EE504", "LEI00005E62FD357EE511", "LEI00005F62FD357EE51E", "LEI00006062FD357EE52A", "LEI00006162FD357EE53F",
    "LEI00006262FD357EE56F", "LEI00006362FD357EE5B6", "LEI00006462FD357EE5C8", "LEI00006562FD357EE5DD", "LEI00006662FD357EE5F4",
    "LEI00006762FD357EE60D", "LEI00006862FD357EE623", "LEI00006962FD357EE634", "LEI00006A62FD357EE645", "LEI00006B62FD357EE652",
    "LEI00006C62FD357EE65F", "LEI00006D62FD357EE670", "LEI00006E62FD357EE681", "LEI00006F62FD357EE6A3", "LEI00007062FD357EE6EF",
    "LEI00007162FD357EE76B", "LEI00007262FD357EE7DE", "LEI00007362FD357EE7FF", "LEI00007462FD357EE818", "LEI00007562FD357EE839",
    "LEI00007662FD357EE86E", "LEI00007762FD357EE880", "LEI00007862FD357EE88D", "LEI00007962FD357EE8B3", "LEI00007A62FD357EE8C7",
    "LEI00007B62FD357EE8D5", "LEI00007C62FD357EE92A", "LEI00007D62FD357EE953", "LEI00007E62FD357EE966", "LEI00007F62FD357EE979",
    "LEI00008062FD357EE9A6", "LEI00008162FD357EE9C8", "LEI00008262FD357EE9F8", "LEI00008362FD357EEA09", "LEI00008462FD357EEA4A",
    "LEI00008562FD357EEA78", "LEI00008662FD357EEA8F", "LEI00008762FD357EEABA", "LEI00008862FD357EEAD8", "LEI00008962FD357EEB1E",
    "LEI00008A62FD357EEB4A", "LEI00008B62FD357EEB84", "LEI00008C62FD357EEBE9", "LEI00008D62FD357EEBFB", "LEI00008E62FD357EEC62",
    "LEI00009062FD357EEC90", "LEI00009162FD357EEC9F", "LEI00009262FD357EECCB", "LEI00009362FD357EECE3", "LEI00009462FD357EEDE3",
    "LEI00009562FD357EEE05", "LEI00009662FD357EEE44", "LEI00009762FD357EEE99", "LEI00009862FD357EEECE", "LEI00009962FD357EEF01",
    "LEI00009A62FD357EEF15", "LEI00009B62FD357EEF24", "LEI00009C62FD357EEF33", "LEI00009D62FD357EEF50", "LEI00009E62FD357EEF5F",
    "LEI00009F62FD357EEFD4", "LEI0000A062FD357EEFE1", "LEI0000A162FD357EF008", "LEI0000A262FD357EF04A", "LEI0000A362FD357EF080",
    "LEI0000A462FD357EF0C9", "LEI0000A562FD357EF0F3", "LEI0000A662FD357EF10A", "LEI0000A762FD357EF134", "LEI0000A862FD357EF14E",
    "LEI0000A962FD357EF175", "LEI0000AA62FD357EF21D", "LEI0000AB62FD357EF252", "LEI0000AC62FD357EF269", "LEI0000AD62FD357EF275",
    "LEI0000AE62FD357EF296", "LEI0000AF62FD357EF2A2", "LEI0000B062FD357EF2B3", "LEI0000B162FD357EF2CF", "LEI0000B262FD357EF2EF",
    "LEI0000B362FD357EF3A9", "LEI0000B462FD357EF3E4", "LEI0000B562FD357EF45E", "LEI0000B662FD357EF4C8", "LEI0000B762FD357EF50C",
    "LEI0000B862FD357EF561", "LEI0000B962FD357EF5B3", "LEI0000BA62FD357EF5F7", "LEI0000BB62FD357EF66F", "LEI0000BC62FD357EF681",
    "LEI0000BD62FD357EF693", "LEI0000BE62FD357EF6B1", "LEI0000BF62FD357EF6CA", "LEI0000C062FD357EF709", "LEI0000C162FD357EF74B",
    "LEI0000C262FD357EF79A", "LEI0000C362FD357EF826", "LEI0000C462FD357EF882", "LEI0000C562FD357EF8A5", "LEI0000CC62FD357EF9BE",
    "LEI0000CD62FD357EF9D9", "LEI0000CE62FD357EFA14", "LEI0000CF62FD357EFA58", "LEI0000D062FD357EFA97", "LEI0000D162FD357EFAE0",
    "LEI0000D262FD357EFB42", "LEI0000D362FD357EFB78", "LEI0000D462FD357EFBAA", "LEI0000D562FD357EFC3D", "LEI0000D662FD357EFCB4",
    "LEI0000D762FD357EFCC2", "LEI0000D862FD357EFCCE", "LEI0000D962FD357EFCDF", "LEI0000DA62FD357EFCEC", "LEI0000DB62FD357EFCFD",
    "LEI0000DC62FD357EFD14", "LEI0000DD62FD357EFD24", "LEI0000DE62FD357EFD41", "LEI0000DF62FD357EFD4E", "LEI0000E062FD357EFD6A",
    "LEI0000E162FD357EFD8F", "LEI0000E262FD357EFDA1", "LEI0000E362FD357EFDC9", "LEI0000E462FD357EFDE1", "LEI0000E562FD357EFE28",
    "LEI0000E662FD357EFE74", "LEI0000E762FD357EFED2", "LEI0000E862FD357EFF05", "LEI0000E962FD357EFF1A", "LEI0000EA62FD357EFF4F",
    "LEI0000EB62FD357E0025", "LEI0000EC62FD357E0037", "LEI0000ED62FD357E0057", "LEI0000EE62FD357E007A", "LEI0000EF62FD357E0099",
    "LEI0000F062FD357E00B2", "LEI0000F162FD357E00CA", "LEI0000F262FD357E00DE", "LEI0000F362FD357E00ED", "LEI0000F462FD357E00FD",
    "LEI0000F562FD357E0116", "LEI0000F662FD357E0125", "LEI0000F762FD357E0135", "LEI0000F862FD357E0144", "LEI0000F962FD357E015D",
    "LEI0000FA62FD357E021D", "LEI0000FB62FD357E02AE", "LEI0000FC62FD357E0336", "LEI0000FD62FD357E03A8", "LEI0000FE62FD357E03F7",
    "LEI0000FF62FD357E049F", "LEI00010062FD357E0556", "LEI00010162FD357E0566", "LEI00010262FD357E0591", "LEI00010362FD357E05BC",
    "LEI00010462FD357E05F2", "LEI00010562FD357E0616", "LEI00010762FD357E0681", "LEI00010862FD357E06C4", "LEI00010962FD357E0795",
    "LEI00010A62FD357E07F9", "LEI00010B62FD357E080C", "LEI00010C62FD357E081B", "LEI0000B162FD357EF2CF_1", "LEI0000FA62FD357E021D_1",
    "LEI0000B162FD357EF2CF_2", "LEI00005962FD357EE289_1", "LEI00005A62FD357EE2C9_1", "LEI00005A62FD357EE2C9_2", "LEI00005A62FD357EE2C9_3",
    "LEI0000E962FD357EFF1A_1", "LEI00009C62FD357EEF33_1", "LEI0000B262FD357EF2EF_1", "LEI0000F962FD357E015D_1", "LEI0000B262FD357EF2EF_2",
    "LEI00002F62FD357EDAD5_1", "LEI00008362FD357EEA09_1", "LEI00002E62FD357EDA82_1", "LEI0000A362FD357EF080_1", "LEI0000A462FD357EF0C9_1",
    "LEI0000C362FD357EF826_1", "LEI0000C562FD357EF8A5_1", "LEI0000A362FD357EF080_2", "LEI0000A462FD357EF0C9_2", "LEI00000B62FD357ED596_1",
    "LEI00007F62FD357EE979_1", "LEI00009662FD357EEE44_1", "LEI00004062FD357EDD76_1", "LEI0000E762FD357EFED2_1", "LEI0000B362FD357EF3A9_1",
    "LEI0000B462FD357EF3E4_1", "LEI0000B562FD357EF45E_1", "LEI0000CF62FD357EFA58_1", "LEI0000CF62FD357EFA58_2", "LEI00005B62FD357EE44A_1",
    "LEI00004662FD357EDEF7_1", "LEI00004562FD357EDEB3_1", "LEI00008862FD357EEAD8_1", "LEI00000762FD357ED46F_1", "LEI0000FD62FD357E03A8_1",
    "LEI0000CD62FD357EF9D9_1", "LEI0000FB62FD357E02AE_1", "LEI00010762FD357E0681_1", "LEI0000CD62FD357EF9D9_2", "LEI0000FC62FD357E0336_1",
    "LEI00001462FD357ED6D3_1", "LEI00001462FD357ED6D3_2", "LEI0000FB62FD357E02AE_2" ]


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