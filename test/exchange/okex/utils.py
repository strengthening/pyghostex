import unittest
import datetime

from pyexchange.okex import utils


class TestUtils(unittest.TestCase):
    def test_get_the_due(self):
        print(utils.get_the_due("quarter"))

    # def test_get_the_quarter(self):
    #     print(utils.get_the_quarter(datetime.datetime.now()))
