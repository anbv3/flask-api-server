import json
import logging
import logging.config
import os
from unittest import TestCase

from run import app


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base_dir, 'logging.json'), 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)

        app.config['TESTING'] = True
        cls.client = app.test_client()
