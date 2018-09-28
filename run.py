import logging

from flask import Flask

from app.controllers.monitor_controller import monitor
from config.config import get_app_config, setup_logging, BASE_DIR

setup_logging()
logging.info("BASE_DIR: %s", BASE_DIR)

app = Flask(__name__)
app.config.from_pyfile(get_app_config())

app.register_blueprint(monitor, url_prefix='/controllers')

if __name__ == '__main__':
    app.run()
