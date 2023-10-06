import logging
import logging.config
import os

import yaml
from dotenv import load_dotenv


def config_log() -> logging.Logger:
    """Configuración del rastreo de eventos

    :return: log object
    :rtype: logging.Logger
    """

    load_dotenv()
    level_log = os.getenv("logging")

    with open("../reveration_time/logging.yaml", "r") as f:
        log_cfg = yaml.safe_load(f.read())

    logging.config.dictConfig(log_cfg)

    logger = logging.getLogger(level_log)

    if level_log == "dev":
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    print(type(logger))

    return logger
