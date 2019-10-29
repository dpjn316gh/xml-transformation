
# --------------------------------------------------------------------
# Copyright (c) 2019 by PayU Latam
# Project name: Project Name title
# Author: Jorge D. Porras jorge.porras@payulatam.com
# Author: Diego Chavez diego.chavez@payulatam.com
# Version: 0.0.1
# --------------------------------------------------------------------
    

from argparse import ArgumentParser


class CliApp:
    """
    Represents the CLI interface of the application.
    """

    def __init__(self):
        self.parser = ArgumentParser(description="Description of the application", epilog="Description of the application")

    def run(self) -> None:
        """ Entry point of the app

        Returns:
            None:
        """
        self.create_cli_interface()
        args = self.parser.parse_args()

        context = AppContext(Configuration(args.config))
        Logger.load_config(context.get_log_config_file())
        Logger.info("Loading XML transformation")

    def create_cli_interface(self) -> None:
        """
        Create the CLI interface.
        Returns:
            None:
        """
        self.parser.add_argument('--version', action='version', version='0.0.1')
        self.parser.add_argument('--config', type=str, required=True, help="config folder is required")


    