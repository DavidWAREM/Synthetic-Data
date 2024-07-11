import logging
import os
from data_loader import DataLoader
from data_process import DataProcessor

def process_file(file_path):
    logging.info(f"Starting file processing")

    # Part for Import the data
    data_loader = DataLoader(file_path)
    df = data_loader.read_txt()

    iterations = 3
    for i in range(iterations):
        logging.info(f"Start iteration {i + 1}")

        # Part for changing the roughness
        data_processor = DataProcessor(df, file_path)
        data_processor.change_friction()
        data_processor.write_dataframe_as_txt(i)

        # Part for import to stanet and callculate and export new CSV file

def main():
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

    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Add handlers to the root logger
    logging.getLogger('').addHandler(file_handler)
    logging.getLogger('').addHandler(console_handler)

    file_path = "C:\\Users\\d.muehlfeld\\weitere Daten\\14_Spechbach_RNAB.TXT"
    process_file(file_path)

if __name__ == '__main__':
    main()
