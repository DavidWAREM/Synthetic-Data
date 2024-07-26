import logging
import os
from data_loader import DataLoader  # Importing the DataLoader class from the data_loader module
from data_process import DataProcessor  # Importing the DataProcessor class from the data_process module
from stanet_process import StanetProcess  # Importing the StanetProcess class from the stanet_process module


def process_file(file_path, file_name):
    """
    Process a single file: load data, modify it, and run STANET import and export.

    :param file_path: Path to the input file
    :param file_name: Name of the input file
    """
    logging.info(f"Starting file processing for {file_name}")

    # Load the data from the text file
    data_loader = DataLoader(file_path)
    df = data_loader.read_txt()

    iterations = 1  # Number of iterations to process
    for i in range(iterations):
        logging.info(f"Start iteration {i} for {file_name}")

        # Change the roughness in the data
        logging.info(f"Changing friction for iteration {i} for {file_name}")
        data_processor = DataProcessor(df, file_path)
        modified_df = data_processor.change_friction()  # Get the modified DataFrame

        # Write the modified data to a new text file
        logging.info(f"Writing modified data to text file for iteration {i} for {file_name}")
        data_processor.write_dataframe_as_txt(modified_df, i)  # Pass the modified DataFrame

        # Import the modified data to STANET, run calculations, and export results to a CSV file
        logging.info(f"Starting STANET import for iteration {i} for {file_name}")
        stanet_processor = StanetProcess(i=i, file_name=file_name)
        stanet_processor.import_data()

        logging.info(f"Starting STANET export for iteration {i} for {file_name}")
        stanet_processor.export_data()

        logging.info(f"Finished iteration {i} for {file_name}")


def main():
    """
    Main function to set up logging, find .TXT files, and process each one.
    """
    # Get the directory of the script being executed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, 'logging.log')

    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG,  # Set the root logger level to DEBUG
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # File handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Remove all handlers associated with the root logger object
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Add handlers to the root logger
    logging.getLogger('').addHandler(file_handler)
    logging.getLogger('').addHandler(console_handler)

    # Directory containing the .txt files
    directory_path = "C:\\Users\\d.muehlfeld\\weitere Daten"

    # Process each .txt file in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".TXT"):
            file_path = os.path.join(directory_path, file_name)
            process_file(file_path, file_name)


if __name__ == '__main__':
    main()
