# Copyright 2023 Sani-Matic Inc. (sanimatic.com)

import logging
from logging import handlers
from dataclasses import dataclass, field

@dataclass
class SaniTrendLogging:
    """Class for automatic logging
    """
    logger_name: str
    logger: logging.Logger = field(init=False)

    def __post_init__(self):
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)
        logger_formatter = logging.Formatter("%(levelname)s %(asctime)s: %(funcName)s @ line %(lineno)d - %(message)s")
        logger_handler = handlers.TimedRotatingFileHandler(f'{self.logger_name}.log', when="midnight", interval=1, backupCount=30)
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)


def main():
    pass

if __name__ == '__main__':
    main()