/* Copyright (c) 2016 Keita Kita
 *
 * This software is released under the MIT License.
 * http://opensource.org/licenses/mit-license.php
 */

package com.github.mikanbako.ri_receiver;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.os.Handler;
import android.os.Looper;

import java.nio.ByteBuffer;

/**
 * Notifier by Bluetooth Law Energy when infrared rays are received.
 */
public final class RiNotifier {
    /**
     * ID start index of bytes in an advertisement record.
     */
    private static final int ID_START_INDEX = 7;

    private BluetoothAdapter mBluetoothAdapter;

    private BluetoothAdapter.LeScanCallback mScanCallback;

    private int mLatestId = -1;

    private final Handler mMainHandler;

    private Runnable mRestartTask;

    public RiNotifier() {
        mMainHandler = new Handler(Looper.getMainLooper());
    }

    public void initialize() {
        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
    }

    public boolean isBluetoothSupported() {
        return mBluetoothAdapter != null;
    }

    private static int getId(byte[] scanRecord) {
        ByteBuffer buffer = ByteBuffer.wrap(scanRecord);

        return buffer.getInt(ID_START_INDEX);
    }

    /**
     * Start to receive infrared rays.
     *
     * @param receiver Receiver of infrared rays.
     */
    public void start(final RiReceiver receiver) {
        if (mScanCallback != null) {
            return;
        }

        mScanCallback = new BluetoothAdapter.LeScanCallback() {
            @Override
            public void onLeScan(BluetoothDevice device, int rssi, byte[] scanRecord) {
                int id = getId(scanRecord);

                if (id != mLatestId) {
                    mLatestId = id;

                    receiver.onRiReceive(id);
                }

                requestRestartLeScan();
            }
        };

        mBluetoothAdapter.startLeScan(mScanCallback);
    }

    private void requestRestartLeScan() {
        mBluetoothAdapter.stopLeScan(mScanCallback);

        mRestartTask = new Runnable() {
            @Override
            public void run() {
                mRestartTask = null;
                mBluetoothAdapter.startLeScan(mScanCallback);
            }
        };

        mMainHandler.post(mRestartTask);
    }

    /**
     * Stop receiving infrared rays.
     */
    public void stop() {
        if (mScanCallback == null) {
            return;
        }

        if (mRestartTask != null) {
            mMainHandler.removeCallbacks(mRestartTask);
            mRestartTask = null;

            return;
        }

        mBluetoothAdapter.stopLeScan(mScanCallback);
        mScanCallback = null;
    }
}
