import subprocess
import logging

class StanetProcess:
    def __init__(self, i):
        self.i = i
        self.STANET_PATH = r"C:\Program Files\STANET\BIN\stanet64.exe"
        self.NETWORK_FILE = r' /N="C:\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\11_Netz_RNAB\14.1_Spechbach_RNAB.STA"'
        self.CONFIG_FILE = r' /CONFIG="C:\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\Config_Spechbach\\"'
        self.IMPORT_DEFINITION = ' /X="Import_Leitungen_Rauheiten_txt"'
        self.TEXT_FILE = fr' /F="C:\Users\d.muehlfeld\weitere Daten\13_Spechbach_RNAB_{self.i}.TXT"'
        self.EXPORT_DEFINITION = ' /Y="CSV"'
        self.EXPORT_FILE = fr' /E="C:\Users\d.muehlfeld\weitere Daten\export_results_{self.i}.csv"'
        self.CALCULATE = ' /B'

        logging.basicConfig(filename='stanet_process.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def run_command(self, cmd):
        """Run the command and log the output."""
        logging.info(f"Executing command: {cmd}")
        try:
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            logging.info(f"Command executed successfully: {cmd}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error occurred while executing command: {cmd}")
            logging.error(e.stderr.decode())  # Log the standard error

    def import_data(self):
        """Build and run the import command."""
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
        command_export = (f'"{self.STANET_PATH}"'
                          f'{self.NETWORK_FILE}'
                          f'{self.CONFIG_FILE}'
                          f'{self.EXPORT_DEFINITION}'
                          f'{self.EXPORT_FILE}'
                          f'{self.CALCULATE}')
        logging.info(f"Preparing to export data for iteration {self.i}")
        self.run_command(command_export)
