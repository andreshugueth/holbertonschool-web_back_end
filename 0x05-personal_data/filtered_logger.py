#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format method to class

        Args:
            record (logging.LogRecord): [description]

        Returns:
            str: [description]
        """
        msg = filter_datum(self.fields, self.REDACTION,
                           super().format(record), self.SEPARATOR)
        return msg


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function called filter_datum

    Args:
        fields (List): a list of strings representing all fields to obfuscate
        redaction (str): a string representing by what
                        the field will be obfuscated
        message (str): a string representing the log line
        separator (str): a string representing by which character is
                        separating all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}",
                         message)
    return message


def get_logger() -> logging.Logger:
    """get_logger implementation

    Returns:
        logging.Logger:
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
