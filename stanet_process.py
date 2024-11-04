import subprocess
import logging

# This class interacts with the STANET software by constructing and executing command-line calls
class StanetProcess:
    def __init__(self, current_number, file_name, with_load=False):
        """
        Initializes the StanetProcess class.

        :param current_number: The current iteration number, used to create unique file names.
        :param file_name: The name of the input file, used for logging and exporting results.
        :param with_load: Boolean flag to determine whether to use files with load or without load.

        The constructor sets paths and parameters for the STANET executable, network file, import/export definitions,
        and other configurations. It also sets up logging to record the execution of commands.
        """
        self.current_number = current_number  # The iteration number to uniquely identify files
        self.file_name = file_name  # Name of the input file used in logging and exporting
        self.with_load = with_load  # Flag to determine whether to use network with load or without load

        # Path to the STANET executable
        self.STANET_PATH = r"C:\Program Files\STANET\BIN\stanet64.exe"

        # Paths to the STANET network files, depending on the with_load flag
        self.NETWORK_FILE_without_load = r' /N="C:\Users\D.Muehlfeld\Documents\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\11_Netz_RNAB\Spechbach_Simplification^3_Roughness_without_load.STA"'
        self.NETWORK_FILE_with_load = r' /N="C:\Users\D.Muehlfeld\Documents\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\11_Netz_RNAB\Spechbach_Simplification^3_Roughness_with_load.STA"'

        # Select the correct network file based on the with_load flag
        self.NETWORK_FILE = self.NETWORK_FILE_with_load if self.with_load else self.NETWORK_FILE_without_load

        # Path to the configuration file that STANET will use
        self.CONFIG_FILE = r' /CONFIG="C:\Users\D.Muehlfeld\Documents\aktuelle Berechnungen\Spechebach_Rechennetzmodell_Wasser\Config_Spechbach"'

        # Import definition, used to specify how STANET should import data
        self.IMPORT_DEFINITION = ' /X="Leitungen_Rauheiten_txt"'

        # Path to the specific text file that will be imported into STANET, dynamically built using current_number
        self.TEXT_FILE = fr' /F="C:\Users\D.Muehlfeld\OneDrive - RBS wave GmbH\Synthetic_Data\Synthetic_Data_Roughness\Import Data\Spechbach_Simplification^3_{self.current_number}.TXT"'

        # Export definition, specifies how STANET should export the data
        self.EXPORT_DEFINITION = ' /Y="CSV"'

        # Paths to the CSV export files, depending on the with_load flag
        self.EXPORT_FILE_without_load = fr' /E="C:\Users\D.Muehlfeld\OneDrive - RBS wave GmbH\Synthetic_Data\Synthetic_Data_Roughness\SyntheticData-Spechbach_Simplification^3_Roughness_without_load_{self.current_number}.csv"'
        self.EXPORT_FILE_with_load = fr' /E="C:\Users\D.Muehlfeld\OneDrive - RBS wave GmbH\Synthetic_Data\Synthetic_Data_Roughness\SyntheticData-Spechbach_Simplification^3_Roughness_with_load_{self.current_number}.csv"'

        # Select the correct export file based on the with_load flag
        self.EXPORT_FILE = self.EXPORT_FILE_with_load if self.with_load else self.EXPORT_FILE_without_load

        # This flag tells STANET to perform calculations after importing or exporting
        self.CALCULATE = ' /B'

        # Set up logging to capture output in 'stanet_process.log', tracking key steps and any errors
        logging.basicConfig(filename='stanet_process.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def run_command(self, cmd):
        """
        Runs the specified command using subprocess and logs the result.

        :param cmd: The command string to be executed.

        This method logs the command being executed and captures both standard output and error streams.
        If the command fails, the error message is logged.
        """
        logging.info(f"Executing command: {cmd}")  # Log the command about to be run
        try:
            # Execute the command via subprocess and capture output (stdout and stderr)
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            logging.info(f"Command executed successfully: {cmd}")  # Log success if the command ran without errors
        except subprocess.CalledProcessError as e:
            # If an error occurs, log both the command and the error output
            logging.error(f"Error occurred while executing command: {cmd}")
            logging.error(e.stderr.decode())  # Decode and log the error message from standard error

    def import_data(self):
        """
        Builds the command to import data into STANET and calls run_command() to execute it.

        This method constructs a command string with paths and flags required to import a text file into STANET.
        The command is then passed to `run_command()` to be executed.
        """
        # Construct the full command for importing data to STANET, including network, config, and text file paths
        command_import = (f'"{self.STANET_PATH}"'
                          f'{self.NETWORK_FILE}'
                          f'{self.CONFIG_FILE}'
                          f'{self.IMPORT_DEFINITION}'
                          f'{self.TEXT_FILE}'
                          ' /A'  # Import flag
                          f'{self.CALCULATE}')  # Calculation flag to run calculations after import

        logging.info(
            f"Preparing to import data for number {self.current_number}")  # Log the start of the import process
        self.run_command(command_import)  # Execute the constructed command

    def export_data(self):
        """
        Builds the command to export data from STANET and calls run_command() to execute it.

        This method constructs a command string with paths and flags required to export results from STANET to a CSV file.
        The command is then passed to `run_command()` to be executed.
        """
        # Construct the full command for exporting data from STANET, including network, config, and export file paths
        command_export = (f'"{self.STANET_PATH}"'
                          f'{self.NETWORK_FILE}'
                          f'{self.CONFIG_FILE}'
                          f'{self.EXPORT_DEFINITION}'
                          f'{self.EXPORT_FILE}'
                          f'{self.CALCULATE}'
                          f' /MED=04:00')  # Calculation flag to run calculations after export

        logging.info(
            f"Preparing to export data for number {self.current_number}")  # Log the start of the export process
        self.run_command(command_export)  # Execute the constructed command
