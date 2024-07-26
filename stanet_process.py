import subprocess
import logging

class StanetProcess:
    def __init__(self, i, file_name):
        # Initialize the instance with the iteration number and file name
        self.i = i
        self.file_name = file_name

        # Define the path to the STANET executable
        self.STANET_PATH = r"C:\Program Files\STANET\BIN\stanet64.exe"

        # Define the path to the network file used by STANET
        self.NETWORK_FILE = r' /N="C:\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\11_Netz_RNAB\14.1_Spechbach_RNAB.STA"'

        # Define the path to the configuration files
        self.CONFIG_FILE = r' /CONFIG="C:\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\Config_Spechbach"'

        # Define the import definition to be used
        self.IMPORT_DEFINITION = ' /X="Import_Leitungen_Rauheiten_txt"'

        # Define the path to the text file for import
        self.TEXT_FILE = fr' /F="C:\Users\d.muehlfeld\weitere Daten\Synthetic_Data\13_Spechbach_RNAB_{self.i}.TXT"'

        # Define the export definition to be used
        self.EXPORT_DEFINITION = ' /Y="CSV"'

        # Define the path for the export file
        self.EXPORT_FILE = fr' /E="C:\Users\d.muehlfeld\weitere Daten\Synthetic_Data\export_results_{self.file_name}_{self.i}.csv"'

        # Define the command to perform calculation
        self.CALCULATE = ' /B'

        # Configure logging settings
        logging.basicConfig(filename='stanet_process.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def run_command(self, cmd):
        """Run the command and log the output."""
        logging.info(f"Executing command: {cmd}")
        try:
            # Execute the command
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            logging.info(f"Command executed successfully: {cmd}")
        except subprocess.CalledProcessError as e:
            # Log any errors that occur during execution
            logging.error(f"Error occurred while executing command: {cmd}")
            logging.error(e.stderr.decode())  # Log the standard error

    def import_data(self):
        """Build and run the import command."""
        # Construct the command for importing data
        command_import = (f'"{self.STANET_PATH}"'
                          f'{self.NETWORK_FILE}'
                          f'{self.CONFIG_FILE}'
                          f'{self.IMPORT_DEFINITION}'
                          f'{self.TEXT_FILE}'
                          ' /A'
                          f'{self.CALCULATE}')
        logging.info(f"Preparing to import data for iteration {self.i}")
        self.run_command(command_import)

    def export_data(self):
        """Build and run the export command."""
        # Construct the command for exporting data
        command_export = (f'"{self.STANET_PATH}"'
                          f'{self.NETWORK_FILE}'
                          f'{self.CONFIG_FILE}'
                          f'{self.EXPORT_DEFINITION}'
                          f'{self.EXPORT_FILE}'
                          f'{self.CALCULATE}')
        logging.info(f"Preparing to export data for iteration {self.i}")
        self.run_command(command_export)
