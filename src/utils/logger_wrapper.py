# --------------------------------------------------------------------
# Copyleft (c) 2019
# Author Jorge Porras<dpjn316@gmail.com>
# Version: 0.0.1
# --------------------------------------------------------------------

import logging
import logging.config
import sys

from himl import ConfigProcessor


class Logger:
    """
    Wrapper for logging.logger
    """

    @classmethod
    def load_config(cls, config_file: str) -> None:
        """
        Loads the log's configuration.
        Args:
            config_file (str): Path of the yaml config file for logging lib.

        Returns:
            None:
        """
        config_processor = ConfigProcessor()

        path = config_file
        filters = ()  # can choose to output only specific keys
        exclude_keys = ()  # can choose to remove specific keys
        output_format = "json"  # yaml/json

        ordered_config_dict = config_processor.process(path=path, filters=filters, exclude_keys=exclude_keys,
                                                       output_format=output_format, print_data=False)
        logging.config.dictConfig(dict(ordered_config_dict))

        cls.logger = logging.getLogger()

    @classmethod
    def load_config_for_unittest(cls):
        """
        Loads the log's configuration for unit tests.
        Returns:
            None:
        """
        cls.logger = logging.getLogger()
        cls.logger.level = logging.DEBUG
        stream_handler = logging.StreamHandler(sys.stdout)
        cls.logger.addHandler(stream_handler)

        cls.logger = logging.getLogger()

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.
        Args:
            msg (str): Message.
            *args: arguments.
            **kwargs: arguments' values.

        Returns:
            None:
        """
        cls.logger.debug(msg, *args, **kwargs)

    @classmethod
    def info(cls, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.
        Args:
            msg (str): Message.
            *args: arguments.
            **kwargs: arguments' values.

        Returns:
            None:
        """
        cls.logger.info(msg, *args, **kwargs)

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.
            msg (str): Message.
            *args: arguments.
            **kwargs: arguments' values.

        Returns:
            None:
        """
        cls.logger.warning(msg, *args, **kwargs)

    @classmethod
    def error(cls, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.
        Args:
            msg:
            *args:
            **kwargs:

        Returns:

        """
        cls.logger.error(msg, *args, **kwargs)

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        """
            msg (str): Message.
            *args: arguments.
            **kwargs: arguments' values.

        Returns:
            None:
        """
        cls.logger.critical(msg, *args, **kwargs)
