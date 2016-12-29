# 赤外線放射エフェクトARシステム

## 動画

https://youtu.be/A28sL0VISwo

## 概要

リモコンから赤外線を放射するエフェクトを表示するデモ用ARシステムです。

本システムは、下記の要素から構成されています。

* Raspberry Pi
* 赤外線センサ
* Androidアプリ

Raspberry Piは、GPIO経由で赤外線センサと接続します。また、Bluetooth Low Energyを用いてAndroidデバイスと連携します。

赤外線センサは、リモコンからの赤外線を受信します。赤外線を検出すると、Raspberry PiはAndroidデバイスにアドバタイジングパケットを送信します。そのパケットを受信したAndroidデバイスは、画面上のリモコンから赤外線が放射されるエフェクトを描きます。

## システム要件

### Raspberry Pi

* bash
* Python 3 + [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
* Bluetooth Low Energy

### 赤外線センサ

赤外線受信モジュール。例：PL-IRM2161-XD1

### Androidデバイス

Bluetooth Low Energyおよびカメラが使用できるAndroid 4.4以上の端末。

## ライセンス

MITライセンスです。詳細は「LICENSE.txt」をご覧ください。

## ディレクトリの内容

### circuit_diagram

Raspberry Piと赤外線センサ（PL-IRM2161-XD1）を接続する回路図。ファイルは、[Fritzing](http://fritzing.org/)で開けます。

### ri_advertiser

赤外線の受信をGPIO経由で検出して、Bluetooth Low Energyでアドバタイジングパケットを送信するPython 3スクリプト。

### RI_AR

カメラからの画像や赤外線放射エフェクトを表示するUnityアプリケーションのプロジェクト。本Unityプロジェクトは下記のサードパーティアセットやSDKを使用しています。

* [Vuforia](https://developer.vuforia.com/) 4.2.3
* [Simple Particle Pack](https://www.assetstore.unity3d.com/jp/#!/content/3045)
* [Elementals](https://www.assetstore.unity3d.com/jp/#!/content/11158) 1.1.1

本Unityプロジェクトに、上記アセット、SDKをインポートしてください。

### ri_receiver

Bluetooth Low Energyのアドバタイジングパケットを受信し、登録されたリスナを呼び出すAndroidライブラリのプロジェクト。本ライブラリは、build.gradle内の「deploy」タスクによって、RI_ARへ配備されます。

## コントリビューション

本システムのサポートは行いません。そのため、ドキュメント関連のPull Request以外を受け付ける予定はありません。
