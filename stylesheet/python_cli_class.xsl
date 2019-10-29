<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:fn="http://www.w3.org/2005/xpath-functions"
                version="1.0">

    <xsl:import href="python_file_header.xsl"/>
    <xsl:output method="text" encoding="UTF-8"/>
    <xsl:template match="project">
        <xsl:apply-imports/>

from argparse import ArgumentParser


class CliApp:
    """
    Represents the CLI interface of the application.
    """

    def __init__(self):
        self.parser = ArgumentParser(description="<xsl:apply-templates select="description/title"/>", epilog="<xsl:apply-templates select="description/title"/>")

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
        self.parser.add_argument('--version', action='version', version='<xsl:apply-templates select="@version"/>')
        self.parser.add_argument('--config', type=str, required=True, help="config folder is required")


    </xsl:template>

</xsl:stylesheet>