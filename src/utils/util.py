__author__ = "Maysam Mokarian"
__email__ = "mamokari@microsoft.com"
__license__ = "MIT"
__version__ = "February 2022"

import yaml
from os.path import exists


class Util(object):
    config_filepath = "config/config.yml"
    if not exists(config_filepath):
        config = None
    else:
        with open(config_filepath, "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
