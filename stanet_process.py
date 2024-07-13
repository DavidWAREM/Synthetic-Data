import subprocess
import logging

# Set up logging
logging.basicConfig(filename='stanet_process.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the paths and filenames
STANET_PATH = r"C:\Program Files\STANET\BIN\stanet64.exe"
NETWORK_FILE = r' /N="C:\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\11_Netz_RNAB\14_Spechbach_RNAB.STA"'
IMPORT_DEFINITION = ' /X=".txt Rauheiten_Import"'
TEXT_FILE = r' /F="C:\Users\d.muehlfeld\weitere Daten\14_Spechbach_RNAB_1.TXT"'
EXPORT_DEFINITION = ' /Y="CSV"'
EXPORT_FILE = r' /E="C:\Users\d.muehlfeld\weitere Daten\export_results.csv"'
NO_USER_CONFIG = ' /NoUserConfig'
NO_START_DIALOGS = ' /NoStartDlogs'
CALCULATE = ' /B'

# Combine all parts into a single command
command = (f'"{STANET_PATH}"'
           f'{NETWORK_FILE}'
           f'{NO_USER_CONFIG}'
           f'{NO_START_DIALOGS}'
        #    f'{IMPORT_DEFINITION}'
        #    f'{TEXT_FILE}'
        #    f'{EXPORT_DEFINITION}'
        #    f'{EXPORT_FILE}'
        #   f'{CALCULATE}')
           )
# Function to run the command and log the output
def run_command(cmd):
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Command executed successfully: {cmd}")
        logging.info(result.stdout.decode())  # Log the standard output
        print(f"Command executed successfully: {cmd}")
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while executing command: {cmd}")
        logging.error(e.stderr.decode())  # Log the standard error
        print(f"Error occurred while executing command: {cmd}")
        print(e.stderr.decode())

# Run the command
run_command(command)
