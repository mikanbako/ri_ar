# Copyright (c) 2016 Keita Kita
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

import unittest
from unittest.mock import MagicMock
from ri_advertiser.ri_advertiser import Gpio, Advertiser, RiAdvertiser


class RiAdvertiserTest(unittest.TestCase):
    def setUp(self):
        self.__gpio = Gpio()
        self.__gpio.initialize()

        self.__advertiser = Advertiser()
        self.__ri_advertiser = RiAdvertiser(self.__gpio, self.__advertiser)

    def tearDown(self):
        self.__gpio.release()

    def test_wait_for_input(self):
        self.__gpio.wait_for_input = MagicMock()
        self.__ri_advertiser.wait_for_input()

        self.__gpio.wait_for_input.assert_called_once_with()

    def test_start_advertise(self):
        self.__advertiser.start = MagicMock()
        self.__ri_advertiser.start_advertise()

        self.__advertiser.start.assert_called_once_with()

    def test_stop_advertise(self):
        self.__advertiser.stop = MagicMock()
        self.__ri_advertiser.stop_advertise()

        self.__advertiser.stop.assert_called_once_with()
