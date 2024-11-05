import logging
import os
from data_loader import DataLoader  # Importing the DataLoader class from the data_loader module
from data_process import DataProcessor  # Importing the DataProcessor class from the data_process module
from stanet_process import StanetProcess  # Importing the StanetProcess class from the stanet_process module

# This function is responsible for processing a single file. It loads the data, modifies it, and interacts with STANET for import and export processes.
def process_file(file_path, file_name, start_number):
    """
    Process a single file: load data, modify it, and run STANET import and export.

    :param file_path: Path to the input file
    :param file_name: Name of the input file
    :param start_number: The starting number for iteration
    """
    logging.info(f"Starting file processing for {file_name}")  # Log the start of processing for the file

    # Initialize the DataLoader class and read the data from the provided text file.
    data_loader = DataLoader(file_path)
    df = data_loader.read_txt()  # Load the data into a DataFrame

    iterations = 15000  # Number of iterations for processing each file
    current_number = start_number  # Start from the specified number

    # Loop over the defined number of iterations (in this case, 3 iterations)
    for i in range(iterations):
        logging.info(
            f"Start iteration {i} (number {current_number}) for {file_name}")  # Log the start of each iteration

        # Modify the friction/roughness values in the DataFrame
        logging.info(f"Changing friction for iteration {i} (number {current_number}) for {file_name}")
        data_processor = DataProcessor(df, file_path)  # Initialize the DataProcessor class
        modified_df = data_processor.change_friction()  # Apply the friction changes and get the modified DataFrame

        # Write the modified data to a new text file
        logging.info(f"Writing modified data to text file for iteration {i} (number {current_number}) for {file_name}")
        data_processor.write_dataframe_as_txt(modified_df, current_number)  # Save the modified DataFrame to a file

        # First: Interact with STANET without load
        logging.info(f"Starting STANET import for iteration {i} (number {current_number}) without load for {file_name}")
        stanet_processor_without_load = StanetProcess(current_number=current_number, file_name=file_name,
                                                      with_load=False)  # Initialize StanetProcess without load
        stanet_processor_without_load.import_data()  # Import the modified data into STANET without load

        logging.info(f"Starting STANET export for iteration {i} (number {current_number}) without load for {file_name}")
        stanet_processor_without_load.export_data()  # Export the processed data from STANET without load

        # Then: Interact with STANET with load
        logging.info(f"Starting STANET import for iteration {i} (number {current_number}) with load for {file_name}")
        stanet_processor_with_load = StanetProcess(current_number=current_number, file_name=file_name,
                                                   with_load=True)  # Initialize StanetProcess with load
        stanet_processor_with_load.import_data()  # Import the modified data into STANET with load

        logging.info(f"Starting STANET export for iteration {i} (number {current_number}) with load for {file_name}")
        stanet_processor_with_load.export_data()  # Export the processed data from STANET with load

        logging.info(
            f"Finished iteration {i} (number {current_number}) for {file_name}")  # Log the end of the iteration

        # Increment the current number for the next iteration or next file
        current_number += 1


# The main function sets up the logging, finds the text files to process, and iterates over them.
def main():
    """
    Main function to set up logging, find .TXT files, and process each one.
    """
    # Get the directory of the script being executed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, 'logging.log')  # Define the path for the log file

    # Setup logging configuration
    logging.basicConfig(
        level=logging.DEBUG,  # Set the root logger level to DEBUG to capture detailed log messages
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Create a file handler to write logs to a file (logging.log) and set it to DEBUG level
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Define log format
    file_handler.setFormatter(file_formatter)

    # Create a console handler to output logs to the console and set it to INFO level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Remove any existing handlers from the root logger (reset logging configuration)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Add the file and console handlers to the root logger
    logging.getLogger('').addHandler(file_handler)
    logging.getLogger('').addHandler(console_handler)

    # Directory containing the .txt files to process
    directory_path = "C:\\Users\\D.Muehlfeld\\OneDrive - RBS wave GmbH\\Synthetic_Data\\Synthetic_Data_Roughness"

    # Define the starting number for iteration (this can be adjusted as needed)
    start_number = 888

    # Iterate over all files in the directory and process each file that ends with ".TXT"
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".TXT"):  # Only process .TXT files
            file_path = os.path.join(directory_path, file_name)  # Get the full path of the file
            process_file(file_path, file_name, start_number)  # Call process_file for the current file

            # Increment the start number for the next file (ensures unique output file names)
            start_number += 1  # You can adjust the increment as needed

# Entry point of the script
if __name__ == '__main__':
    main()  # Call the main function to begin execution
