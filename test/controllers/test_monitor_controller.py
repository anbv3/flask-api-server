import logging
import logging.config

from test.base_test import BaseTest


class TestMonitorController(BaseTest):
    @classmethod
    def setUpClass(cls):
        super(TestMonitorController, cls).setUpClass()

    def test_is_alive(self):
        logging.debug("test alive")
        rv = self.client.get("/monitor/alive")
        logging.debug(rv.status_code)
        logging.debug(rv.data)

    def test_hello(self):
        logging.debug("test alive")
        rv = self.client.get("/monitor/hello")
        logging.debug(rv.status_code)
        logging.debug(rv.data)
