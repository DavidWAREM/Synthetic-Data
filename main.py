import logging
import os



def process_file():
    logging.info(f"Starting file processing")

    # Part for Import the data

    iterations = 3
    for i in range(iterations):
        logging.info(f"Start iteration {i + 1}")

        data_processor = DataProcessor()
        # Part for changing the roughness

        # Part for import to stanet and callculate and export new CSV file



def main():
    # Get the directory of the script being executed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, 'logging.log')

    # Setup logging
    logging.basicConfig(
        filename=log_file,
        filemode='w',  # Overwrite the log file on each run
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Add console handler to log to console as well
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)  # Log info level and above to console
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)




if __name__ == '__main__':
    main()
    logging.info("Logging steup is complete")
