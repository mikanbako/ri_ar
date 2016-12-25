#!/usr/bin/env python3

# Copyright (c) 2016 Keita Kita
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

import atexit
import subprocess

try:
    import RPi.GPIO as GPIO
except ImportError:
    pass


class Gpio:
    '''
    Interface for GPIO.
    '''

    def initialize(self):
        pass

    def wait_for_input(self):
        raise NotImplementedError()

    def release(self):
        pass


class RaspberryPiGpio(Gpio):
    '''
    GPIO on Raspberry Pi.
    '''

    # Using GPIO Pin.
    GPIO_PIN = 7

    def initialize(self):
        Gpio.initialize(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GPIO_PIN, GPIO.IN)

    def wait_for_input(self):
        GPIO.wait_for_edge(self.GPIO_PIN, GPIO.RISING)

    def release(self):
        Gpio.release(self)
        GPIO.cleanup()


class Advertiser:
    '''
    Advertise with ID.

    This class is abstract.
    '''

    # Company identifier for test purpose only.
    #
    # See https://www.bluetooth.com/specifications/assigned-numbers/company-Identifiers  # noqa: E501
    COMPANY_IDENTIFIER_CODE = 0xffff

    def __init__(self):
        self.__id = 0

    def start(self):
        self.on_advertise_started(self.create_hci_command())

    def stop(self):
        self.on_advertise_stopped()

    def on_advertise_started(self, hci_command):
        raise NotImplementedError()

    def on_advertise_stopped(self):
        raise NotImplementedError()

    def create_hci_command(self):
        self.__id += 1

        return '0x08 0x0008 0b 02 01 04 07 ff' + \
            ' {:02x}'.format((self.COMPANY_IDENTIFIER_CODE & 0xff00) >> 8) + \
            ' {:02x}'.format(self.COMPANY_IDENTIFIER_CODE & 0x00ff) + \
            ' {:02x}'.format((self.__id & 0xff000000) >> 32) + \
            ' {:02x}'.format((self.__id & 0x00ff0000) >> 16) + \
            ' {:02x}'.format((self.__id & 0x0000ff00) >> 8) + \
            ' {:02x}'.format(self.__id & 0x000000ff) + \
            ' 00' * 20


class BlueZAdvertiser(Advertiser):
    '''
    Advertiser by BlueZ.
    '''

    def on_advertise_started(self, hci_command):
        subprocess.call('hciconfig hci0 noleadv', shell=True)

        hcitool = 'hcitool -i hci0 cmd ' + hci_command
        subprocess.call(hcitool, shell=True)
        subprocess.call('hciconfig hci0 leadv 3', shell=True)
        print(hcitool)

    def on_advertise_stopped(self):
        subprocess.call('hciconfig hci0 noleadv', shell=True)


class RiAdvertiser:
    '''
    Manages GPIO and advertiser objects.
    '''

    def __init__(self, gpio, advertiser):
        self.__gpio = gpio
        self.__advertiser = advertiser

        atexit.register(self.__gpio.release)

    def wait_for_input(self):
        self.__gpio.wait_for_input()

    def start_advertise(self):
        self.__advertiser.start()

    def stop_advertise(self):
        self.__advertiser.stop()


def main():
    gpio = RaspberryPiGpio()
    gpio.initialize()

    ri_advertiser = RiAdvertiser(gpio, BlueZAdvertiser())

    while True:
        ri_advertiser.wait_for_input()
        ri_advertiser.stop_advertise()
        ri_advertiser.start_advertise()


if __name__ == '__main__':
    main()
