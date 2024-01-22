import os
import yaml
from dotenv import load_dotenv
from pathlib import Path


def load_config():
    root_dir = Path(__file__).resolve().parents[2]
    config_file_path = root_dir.joinpath('config.yml')
    with open(config_file_path, 'r') as config_file:
        try:
            config = yaml.safe_load(config_file)
        except yaml.YAMLError as err:
            print(err)
    return config


def set_environment_variables(config):
    load_dotenv(config['credentials'])
    user_agent = os.getenv('USER_AGENT')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    if user_agent is not None:
        os.environ['USER_AGENT'] = user_agent
    else:
        print(f'missing key user_agent')

    if client_id is not None:
        os.environ['CLIENT_ID'] = client_id
    else:
        print(f'missing key client_id')

    if client_secret is not None:
        os.environ['CLIENT_SECRET'] = client_secret
    else:
        print(f'missing key client secret')