# Infrared radiation effect AR system

## Movie

https://youtu.be/A28sL0VISwo

## Summary

An AR system for demonstration that shows infrared radiation effects from the remote control.

This system is composed of the following parts.

* Raspberry Pi
* Infrared rays sensor
* Android application

Raspberry Pi connects the infrared rays sensor by GPIO. And it comminucates with the Android application on the device by Bluetooth Low Energy.

The infrared rays sensor receives infrared rays from the remote control. When it receives an infrared ray, Raspberry Pi broadcasts the advertising packet to the Android device. When the device receives the packet, the Android application draws infrared radiation effects from the remote control shown the display.

## System requrements

### Raspberry Pi

* bash
* Python 3 + [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
* BlueZ
* Bluetooth Low Energy

### Infrared rays sensor

Infrared remote control receiver module. For example, PL-IRM2161-XD1.

### Android device

Android 4.4 and above with Bluetooth Low Energy and camera.

## License

The MIT License. See "LICENSE.txt".

## Contents of directories

### circuit_diagram

The circuit diagram that connects the Raspberry Pi and the infrared rays sensor (PL-IRM2161-XD1). The diagram could open with [Fritzing](http://fritzing.org/).

### ri_advertiser

The Python 3 script that detects the infrared reception by GPIO and broadcasts advertising packets by Bluetooth Low Energy.

### RI_AR

The project of Unity application that shows images from the camera and infrared radiation effects. This Unity project uses 3rd party assets and SDK:

* [Vuforia](https://developer.vuforia.com/) 4.2.3
* [Simple Particle Pack](https://www.assetstore.unity3d.com/jp/#!/content/3045)
* [Elementals](https://www.assetstore.unity3d.com/jp/#!/content/11158) 1.1.1

Please import above assets to this Unity project.

### ri_receiver

The project of Android library that receives advertising packets by Bluetooth Low Energy and calls the registered listener. This library is deployed to RI_AR by "deploy" task on build.gradle.

## Contribution

This system is no longer supported. Therefore pull requests will not be accepted except related with documentation.