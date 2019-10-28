# --------------------------------------------------------------------
# Copyleft (c) 2019
# Author Jorge Porras<dpjn316@gmail.com>
# Version: 0.0.1
# --------------------------------------------------------------------
from himl import ConfigProcessor

from utils.logger_wrapper import Logger


class Configuration:
    """
    Map configuration settings from a yaml file to a dictionary
    """
    LOG_CONFIG_FILE = "log_config_file"
    STYLESHEET_PATH = "stylesheet_path"
    OUTPUT_DIR = "output_dir"
    INPUT_DIR = "input_dir"

    def __init__(self, filename: str):
        """
        Initializer for `Configuration` class
        Args:
            filename (str): File where you've got application settings.
        """
        self.filename = filename

    @property
    def getfile(self) -> str:
        """
        Gets the file name of the configuration file.
        Returns:
            str: Gets the file name of the configuration file.
        """
        return self.filename

    def load_config(self) -> dict:
        """
        Loads the configuration from a yaml file into a dictionary.
        Returns:
            dict: All configuration loaded from a yaml file.
        """

        try:

            config_processor = ConfigProcessor()

            path = self.filename
            filters = ()  # can choose to output only specific keys
            exclude_keys = ()  # can choose to remove specific keys
            output_format = "json"  # yaml/json

            ordered_config_dict = config_processor.process(path=path, filters=filters, exclude_keys=exclude_keys,
                                                           output_format=output_format, print_data=False)

            cfg = dict(ordered_config_dict)
            if not isinstance(cfg, dict):
                raise AssertionError("Invalid format of the config file.")
            return cfg
        except Exception as exc:
            Logger.critical(f"Hum, this {self.getfile} file smells awful. Check it out. {exc} I can't "
                            f"continue.")
            raise
