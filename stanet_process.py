import subprocess
import logging

# Set up logging
logging.basicConfig(filename='stanet_process.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the paths and filenames
STANET_PATH = r"C:\Program Files\STANET\BIN\stanet64.exe"
NETWORK_FILE = r' /N="C:\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\11_Netz_RNAB\14.1_Spechbach_RNAB.STA"'
CONFIG_FILE = r' /CONFIG="C:\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\Config_Spechbach\\"'
IMPORT_DEFINITION = ' /X="Import_Leitungen_Rauheiten_txt"'
TEXT_FILE = r' /F="C:\Users\d.muehlfeld\weitere Daten\13_Spechbach_RNAB.TXT"'
EXPORT_DEFINITION = ' /Y="CSV"'
EXPORT_FILE = r' /E="C:\Users\d.muehlfeld\weitere Daten\export_results.csv"'
CALCULATE = ' /B'
NO_USER_CONFIG = ' /NoUserConfig'
NO_START_DIALOGS = ' /NoStartDlogs'

# Combine all parts into a single command
command_import = (f'"{STANET_PATH}"'
           f'{NETWORK_FILE}'
           f'{CONFIG_FILE}'
           f'{IMPORT_DEFINITION}'
           f'{TEXT_FILE}'
            + ' /A'
#           f'{NETWORK_FILE}'
#           f'{EXPORT_DEFINITION}'
 #          f'{EXPORT_FILE}'
           f'{CALCULATE}')


command_export = (f'"{STANET_PATH}"'
           f'{NETWORK_FILE}'
           f'{CONFIG_FILE}'
#           f'{IMPORT_DEFINITION}'
#           f'{TEXT_FILE}'
#            + ' /A'
#           f'{NETWORK_FILE}'
           f'{EXPORT_DEFINITION}'
           f'{EXPORT_FILE}'
           f'{CALCULATE}')


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
run_command(command_import)
run_command(command_export)
