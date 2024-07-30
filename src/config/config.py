import os
from dotenv import load_dotenv
import yaml


class Config(object):
    with open(os.path.join(os.path.dirname(__file__), "config.yaml"), 'r') as stream:
        config = yaml.safe_load(stream)

    NOSQL_USERNAME = config['NOSQL_USERNAME']
    NOSQL_PASSWORD = config['NOSQL_PASSWORD']
    NOSQL_HOST = config['NOSQL_HOST']
    NOSQL_PORT = config['NOSQL_PORT']
    DB_NAME = config['DB_NAME']
