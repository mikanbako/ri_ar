/* Copyright (c) 2016 Keita Kita
 *
 * This software is released under the MIT License.
 * http://opensource.org/licenses/mit-license.php
 */

using UnityEngine;
using UnityEngine.Events;

public class BleReceiver : MonoBehaviour {
    [SerializeField]
    private UnityEvent _riReceivedEvent = new UnityEvent();

    private AndroidJavaObject _riNotificator;

    // Use this for initialization
    private void Start ()
    {
        _riNotificator = new AndroidJavaObject(
            "com.github.mikanbako.ri_receiver.RiNotifier");

        _riNotificator.Call("initialize");

        if (!_riNotificator.Call<bool>("isBluetoothSupported"))
        {
            Application.Quit();
            return;
        }

        _riNotificator.Call(
            "start", new RiReceiver(_riReceivedEvent));
    }

    private void OnDestroy()
    {
        _riNotificator.Call("stop");
    }

    private sealed class RiReceiver : AndroidJavaProxy
    {
        private readonly UnityEvent _riReceivedEvent;

        public RiReceiver(UnityEvent riReceivedEvent) :
        base("com.github.mikanbako.ri_receiver.RiReceiver")
        {
            _riReceivedEvent = riReceivedEvent;
        }

        private void onRiReceive(int id)
        {
            _riReceivedEvent.Invoke();
        }
    }
}
