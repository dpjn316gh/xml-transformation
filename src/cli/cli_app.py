# --------------------------------------------------------------------
# Copyleft (c) 2019
# Author Jorge Porras<dpjn316@gmail.com>
# Version: 0.0.1
# --------------------------------------------------------------------
from argparse import ArgumentParser

from cli.app_context import AppContext
from cli.config import Configuration
from processor.xslt_processor import XsltProcessor
from utils.logger_wrapper import Logger


class CliApp:
    """
    Represents a CLI application.
    """

    def __init__(self):
        self.parser = ArgumentParser(description="XML Transformation", epilog='Enjoy the program! :)')

    def run(self) -> None:
        """ Entry point of the app

        Returns:
            None:
        """
        self.create_cli_interface()
        args = self.parser.parse_args()

        xml_file = "/home/jorge/PycharmProjects/xml-transformation/input_dir/business_class.xml"
        xsl_file = "/home/jorge/PycharmProjects/xml-transformation/stylesheet/business_class.xsl"

        context = AppContext(Configuration(args.config))
        Logger.load_config(context.get_log_config_file())
        Logger.info("Loading XML transformation")
        XsltProcessor.transform(xml_file, xsl_file, context.get_output_dir())

    def create_cli_interface(self) -> None:
        """
        Create the CLI interface.
        Returns:
            None:
        """
        self.parser.add_argument('--version', action='version', version='0.0.1')
        self.parser.add_argument('--config', type=str, required=True, help="yaml config file is required")
