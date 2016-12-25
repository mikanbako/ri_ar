# Copyright (c) 2016 Keita Kita
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

import unittest
from unittest.mock import MagicMock
from ri_advertiser.ri_advertiser import Advertiser


class AdvertiserTest(unittest.TestCase):
    def setUp(self):
        self.__advertiser = Advertiser()

    def test_advertiser_start(self):
        self.__advertiser.on_advertise_started = MagicMock()
        self.__advertiser.on_advertise_stopped = MagicMock()

        self.__advertiser.start()
        self.__advertiser.stop()

        self.__advertiser.on_advertise_started.assert_called_with(
            '0x08 0x0008 0b 02 01 04 07 ff ff ff 00 00 00 01' + ' 00' * 20)

        self.__advertiser.start()
        self.__advertiser.stop()

        self.__advertiser.on_advertise_started.assert_called_with(
            '0x08 0x0008 0b 02 01 04 07 ff ff ff 00 00 00 02' + ' 00' * 20)

    def test_advertiser_stop(self):
        self.__advertiser.on_advertise_started = MagicMock()
        self.__advertiser.on_advertise_stopped = MagicMock()

        self.__advertiser.start()
        self.__advertiser.stop()

        self.__advertiser.on_advertise_stopped.assert_called_once_with()
