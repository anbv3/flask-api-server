import json
import logging
import logging.config
import os

from os.path import dirname

BASE_DIR = dirname(os.path.abspath(os.path.dirname(__file__)))

APP_ALIVE = True

config_log = {
    "development": "dev/logging.json",
    "production": "real/logging.json"
}

config_app = {
    "development": "dev/app.cfg",
    "production": "real/app.cfg"
}


def get_app_config(env_key='FLASK_ENV'):
    env_name = os.getenv(env_key, "development")
    dir_name = config_app[env_name]
    config_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), dir_name))
    return config_path


def setup_logging(env_key='FLASK_ENV'):
    env_name = os.getenv(env_key, "development")
    dir_name = config_log[env_name]
    cfg_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), dir_name)

    if os.path.exists(cfg_dir):
        with open(cfg_dir, 'rt') as f:
            logging.config.dictConfig(json.load(f))
    else:
        logging.basicConfig(level=logging.INFO)
    logging.info("*** LOAD CONFIG FILE: %s ***", cfg_dir)
