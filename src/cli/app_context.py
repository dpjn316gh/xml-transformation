# --------------------------------------------------------------------
# Copyleft (c) 2019
# Author Jorge Porras<dpjn316@gmail.com>
# Version: 0.0.1
# --------------------------------------------------------------------
from cli.config import Configuration


class AppContext:
    """
    Represents the context of the application.

    Basically you can find some useful paths you will need them.
    """

    def __init__(self, config: Configuration):
        self.config = config.load_config()

        self.log_config_file = self.config[Configuration.LOG_CONFIG_FILE]
        self.stylesheet_path = self.config[Configuration.STYLESHEET_PATH]
        self.output_dir = self.config[Configuration.OUTPUT_DIR]
        self.input_dir = self.config[Configuration.INPUT_DIR]

    def get_log_config_file(self):
        return self.log_config_file

    def get_stylesheet_path(self):
        return self.stylesheet_path

    def get_output_dir(self):
        return self.output_dir

    def get_input_dir(self):
        return self.input_dir
